import json, os


class AIAnalyzer:
    """Gemini adapter with a deterministic offline analysis fallback."""
    RULES = [
        (("fire", "shock", "exposed", "leakage", "medical", "ragging"), "Critical", "Maintenance", "Electrical", "Immediate", "Arun Kumar"),
        (("projector", "equipment", "door", "broken"), "High", "Equipment", "Maintenance", "8 hours", "Ravi Das"),
        (("wifi", "internet", "network", "slow"), "Medium", "Network", "IT", "24 hours", "Priya Shah"),
        (("clean", "paint", "suggestion", "furniture"), "Low", "Cleaning", "Housekeeping", "48 hours", "Ravi Das")]

    def analyze(self, text):
        key = os.getenv("GEMINI_API_KEY")
        if key:
            try: return self._gemini(text, key)
            except Exception: pass
        low = text.lower()
        for terms, priority, category, department, eta, technician in self.RULES:
            if any(x in low for x in terms):
                return {"category":category,"priority":priority,"department":department,"expected_time":eta,"technician":technician,"summary":text[:110],"confidence":0.82,"source":"Local smart rules"}
        return {"category":"Other","priority":"Medium","department":"Administration","expected_time":"24 hours","technician":"Unassigned","summary":text[:110],"confidence":0.55,"source":"Local smart rules"}

    def _gemini(self, text, api_key):
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        prompt = '''Classify this campus complaint. Return JSON only with category, priority (Critical/High/Medium/Low), department, expected_time, technician, summary, confidence (0..1). Complaint: ''' + text
        result = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt).text.strip().replace("```json", "").replace("```", "")
        data=json.loads(result); data["source"]="Gemini"; return data
