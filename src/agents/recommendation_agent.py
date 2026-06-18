class RecommendationAgent:

    def execute(self, risks):
        recommendations = []
        for risk in risks:
            risk_lower = risk.lower()
            if "delayed delivery" in risk_lower:
                recommendations.append("Expedite shipments and notify affected stakeholders.")
            elif "pending order" in risk_lower:
                recommendations.append("Closely monitor pending orders and escalate if delays persist.")
            elif "inventory shortage" in risk_lower:
                recommendations.append("Increase inventory replenishment and review safety stock levels.")
            elif "missing inventory information" in risk_lower:
                recommendations.append("Validate inventory records immediately.")
            elif "high transportation cost" in risk_lower:
                recommendations.append("Review logistics contracts and optimize transportation routes.")

        return list(set(recommendations))
    
    