def time_manager(sections: int = 1, duration: float = 1, step_function = "equal"):
    return {"total": float(duration), "perSectionTime": duration/sections}