
"""Сборка отчёта по скважине: факт, прогноз, рабочая точка."""

def build_report(server, well_id: str, horizon_months: int = 12) -> dict:
    """Один отчёт из трёх вызовов MCP. У каждого числа — единица и источник."""
    

    history = server.call("get_production_history", well_id=well_id, months=24)
    

    forecast = server.call("forecast_production", well_id=well_id, history=history, months=horizon_months)
    

    opened = server.call("open_well_model", well_id=well_id)
    nodal = server.call("run_nodal_analysis", session_id=opened["session_id"])
    

    last_month_data = history["points"][-1]
    
    report = {
        "last_fact": {
            "date": last_month_data["date"],
            "q": last_month_data["q_m3_day"],
            "unit": history["units"]["q_m3_day"],
            "source": "get_production_history"
        },
        "forecast": {
            "first_q": forecast["points"][0]["q_m3_day"],
            "last_q": forecast["points"][-1]["q_m3_day"],
            "annual_decline": forecast["fit"]["annual_decline"],
            "r2": forecast["fit"]["r2"],
            "unit": forecast["units"]["q_m3_day"],
            "source": "forecast_production"
        },
        "working_point": {
            "q": nodal["operating_point"]["q_m3_day"],
            "pwf": nodal["operating_point"]["pwf_bar"],
            "unit_q": nodal["units"]["q_m3_day"],
            "unit_pwf": nodal["units"]["pwf_bar"],
            "source": "run_nodal_analysis"
        }
    }
    
    return report
