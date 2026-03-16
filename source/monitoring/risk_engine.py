import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
import os


class RiskEngine:
    def __init__(self):
        self.model = None
        self.model_path = os.path.join(os.path.dirname(__file__), 'risk_model.pkl')
        self.ensure_model_exists()

    def ensure_model_exists(self):
        """Trains a dummy model if one doesn't exist to handle the new 18-feature shape."""
        if not os.path.exists(self.model_path):
            # Dummy data: 17 raw params + 1 CI
            # Columns: turb, ph, ecoli, nit, do, bod, cod, nitri, amm, flu, chl, sul, pb, as, hg, cd, fe, ci
            X = np.array([
                [2.0, 7.0, 0, 10.0, 8.0, 1.0, 10.0, 0.1, 0.1, 0.5, 50, 20, 0.0, 0.0, 0.0, 0.0, 0.1, 10],   # Low risk
                [8.0, 7.0, 0, 20.0, 6.0, 5.0, 30.0, 0.5, 0.5, 1.0, 150, 100, 0.01, 0.01, 0.0, 0.0, 0.2, 35], # Moderate
                [3.0, 5.0, 0, 15.0, 5.0, 3.0, 20.0, 0.2, 0.3, 0.8, 100, 50, 0.02, 0.0, 0.0, 0.0, 0.5, 30],   # Moderate (pH)
                [6.0, 8.0, 1, 50.0, 3.0, 10.0, 60.0, 1.5, 2.0, 2.0, 300, 300, 0.05, 0.05, 0.01, 0.01, 1.0, 80], # High risk
                [10.0, 9.0, 1, 60.0, 1.0, 20.0, 100.0, 3.0, 5.0, 4.0, 500, 500, 0.2, 0.1, 0.05, 0.05, 2.5, 95], # Very High risk
                [1.0, 7.2, 0, 5.0, 9.0, 0.5, 5.0, 0.0, 0.0, 0.2, 20, 10, 0.0, 0.0, 0.0, 0.0, 0.0, 5],      # Safe
            ])
            y = np.array([0, 0, 1, 1, 1, 0])  # 0=Safe, 1=Risky

            model = LogisticRegression(max_iter=1000)
            model.fit(X, y)

            with open(self.model_path, 'wb') as f:
                pickle.dump(model, f)
            self.model = model
        else:
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)

    def calculate_contamination_index(self, turbidity, ph, ecoli_present, nitrate,
                                      do, bod, cod, nitrite, ammonia, fluoride,
                                      chloride, sulphate, lead, arsenic, mercury, cadmium, iron):
        """Calculates Contamination Index based on all parameter rules."""
        index = 0
        if turbidity > 5: index += 10
        if not (6.5 <= ph <= 8.5): index += 10
        if ecoli_present: index += 30
        if nitrate > 45: index += 10
        
        # New Chemical Rules
        if do < 4.0: index += 10
        if bod > 5.0: index += 10
        if cod > 20.0: index += 10
        if fluoride > 1.5: index += 10
        
        # Heavy Metals (Instant High Risk)
        if lead > 0.01 or arsenic > 0.01 or mercury > 0.001 or cadmium > 0.003:
            index += 50
            
        return min(index, 100)

    def predict_risk(self, turbidity, ph, ecoli_present, nitrate,
                     do, bod, cod, nitrite, ammonia, fluoride,
                     chloride, sulphate, lead, arsenic, mercury, cadmium, iron):
        """Predicts risk probability using ML model with all 18 features."""
        # Calculate CI
        ci = self.calculate_contamination_index(
            turbidity, ph, ecoli_present, nitrate,
            do, bod, cod, nitrite, ammonia, fluoride,
            chloride, sulphate, lead, arsenic, mercury, cadmium, iron
        )

        ecoli_val = 1 if ecoli_present else 0
        features = np.array([[
            turbidity, ph, ecoli_val, nitrate,
            do, bod, cod, nitrite, ammonia, fluoride,
            chloride, sulphate, lead, arsenic, mercury, cadmium, iron, ci
        ]])

        try:
            risk_prob = self.model.predict_proba(features)[0][1] * 100
        except ValueError:
            # Model shape mismatch (old model file), recreate it
            os.remove(self.model_path)
            self.ensure_model_exists()
            risk_prob = self.model.predict_proba(features)[0][1] * 100

        return ci, round(risk_prob, 2)

    def generate_insights(self, turbidity, ph, ecoli_present, nitrate,
                          do, bod, cod, nitrite, ammonia, fluoride,
                          chloride, sulphate, lead, arsenic, mercury, cadmium, iron):
        """Generates cause, effect, and remedy based on advanced parameters."""
        causes = []
        effects = []
        remedies = []

        if ecoli_present:
            causes.append("Fecal contamination from sewage or animal waste.")
            effects.append("High risk of waterborne diseases like Cholera, Typhoid.")
            remedies.append("Immediate boiling of water. Chlorination.")

        if turbidity > 5:
            causes.append("High suspended solids from soil erosion.")
            effects.append("Can shelter pathogens.")
            remedies.append("Filtration using sand filters.")

        if ph < 6.5 or ph > 8.5:
            causes.append("Abnormal pH level.")
            effects.append("Can cause corrosion or reduce chlorination efficiency.")
            remedies.append("pH adjustment using neutralizers.")

        # Chemical Insights
        if nitrate > 45 or nitrite > 3:
            causes.append("Agricultural runoff from fertilizers.")
            effects.append("Blue baby syndrome and risk to infants.")
            remedies.append("Reverse osmosis. Boiling DOES NOT remove nitrates.")
            
        if fluoride > 1.5:
            causes.append("Natural geological deposits or industrial waste.")
            effects.append("Dental fluorosis; skeletal fluorosis at high levels.")
            remedies.append("Activated alumina or bone charcoal filtration.")

        # Heavy Metal Insights
        metals = []
        if lead > 0.01: metals.append('Lead')
        if arsenic > 0.01: metals.append('Arsenic')
        if mercury > 0.001: metals.append('Mercury')
        if cadmium > 0.003: metals.append('Cadmium')
        
        if metals:
            causes.append(f"Heavy metal contamination ({', '.join(metals)}) from industrial discharge or pipe corrosion.")
            effects.append("Severe neurological damage, organ failure, and cancer risk.")
            remedies.append("IMMEDIATE DO NOT USE ORDER. Requires specialized ion exchange or RO filtration.")

        if not causes:
            causes.append("Parameters are within safe limits.")
            effects.append("Safe for general use.")
            remedies.append("Routine monitoring and source hygiene.")

        return " ".join(causes), " ".join(effects), " ".join(remedies)

    def determine_alert_level(self, risk_score):
        """Determines alert level based on risk score."""
        if risk_score > 70:
            return 'Red'
        elif risk_score >= 30:
            return 'Yellow'
        else:
            return 'Green'
