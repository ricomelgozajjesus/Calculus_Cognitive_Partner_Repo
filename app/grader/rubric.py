from typing import Any, Dict
import sympy as sp

# app/grader/rubric.py
def grade_mcq(question: dict, chosen_idx: int) -> dict:
    correct_idx = question.get("answer_index", 0)
    return {"correct": int(chosen_idx) == int(correct_idx)}

def grade_symbolic(expr_str: str, user_answer: str, var: str = "x") -> Dict[str, Any]:
    x = sp.symbols(var)
    try:
        target = sp.simplify(expr_str)
        attempt = sp.simplify(user_answer)
        ok = sp.simplify(target - attempt) == 0
        return {"correct": bool(ok)}
    except Exception:
        return {"correct": False, "error": "parse"}
