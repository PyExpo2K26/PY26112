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
        """Trains a dummy model if one doesn't exist."""
        if not os.path.exists(self.model_path):
            # Dummy data for training
            # Features: [turbidity, ph, ecoli_present (0/1), nitrate, contamination_index]
            X = np.array([
                [2.0, 7.0, 0, 10.0, 10],   # Low risk
                [8.0, 7.0, 0, 20.0, 35],   # Moderate
                [3.0, 5.0, 0, 15.0, 30],   # Moderate (pH)
                [6.0, 8.0, 1, 50.0, 80],   # High risk
                [10.0, 9.0, 1, 60.0, 95],  # Very High risk
                [1.0, 7.2, 0, 5.0, 5],     # Safe
            ])
            y = np.array([0, 0, 1, 1, 1, 0])  # 0=Safe, 1=Risky

            model = LogisticRegression()
            model.fit(X, y)

            with open(self.model_path, 'wb') as f:
                pickle.dump(model, f)
            self.model = model
        else:
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)

    def calculate_contamination_index(self, turbidity, ph, ecoli_present, nitrate):
        """Calculates Contamination Index based on rules."""
        index = 0
        if turbidity > 5:
            index += 25
        if not (6.5 <= ph <= 8.5):
            index += 20
        if ecoli_present:
            index += 40
        if nitrate > 45:
            index += 15
        return min(index, 100)

    def predict_risk(self, turbidity, ph, ecoli_present, nitrate):
        """Predicts risk probability using ML model."""
        ci = self.calculate_contamination_index(turbidity, ph, ecoli_present, nitrate)

        # Prepare features for ML
        ecoli_val = 1 if ecoli_present else 0
        features = np.array([[turbidity, ph, ecoli_val, nitrate, ci]])

        # Get probability of class 1 (High Risk)
        risk_prob = self.model.predict_proba(features)[0][1] * 100
        return ci, round(risk_prob, 2)

    def generate_insights(self, turbidity, ph, ecoli_present, nitrate):
        """Generates cause, effect, and remedy based on water parameters."""
        causes = []
        effects = []
        remedies = []

        if ecoli_present:
            causes.append("Fecal contamination from sewage or animal waste.")
            effects.append("High risk of waterborne diseases like Cholera, Typhoid, or Dysentery.")
            remedies.append("Immediate boiling of water. Chlorination of the water source.")

        if turbidity > 5:
            causes.append("High suspended solids from soil erosion or runoff.")
            effects.append("Can shelter pathogens. Aesthetically unpleasing.")
            remedies.append("Filtration using sand or activated carbon filters.")

        if ph < 6.5:
            causes.append("Acidic water from industrial runoff or mineral deposits.")
            effects.append("Corrosion of pipes leading to heavy metal leaching.")
            remedies.append("Use neutralizing filters or add soda ash.")
        elif ph > 8.5:
            causes.append("Alkaline water from limestone bedrock.")
            effects.append("Decreased efficiency of chlorination.")
            remedies.append("Reverse osmosis or add a weak acid.")

        if nitrate > 45:
            causes.append("Agricultural runoff from fertilizers.")
            effects.append("Blue baby syndrome in infants.")
            remedies.append("Reverse osmosis or ion exchange. Boiling DOES NOT remove nitrates.")

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
