from fastapi import HTTPException

from services.ai import analyze_error


async def send_log(log: str):
    mapped_errors = {
        "ZeroDivisionError: division by zero": {
            "summary": "occurs when you attempt to divide a number by zero or use the modulo operator (%) with a zero divisor.",
            "severity": "low",
        },
        "TypeError": {
            "summary": "raised when an operation or function is applied to an object of an inappropriate data type",
            "severity": "low",
        },
        "ValueError": {
            "summary": "occurs when a function or operation receives an argument that is the correct type but has an inappropriate value",
            "severity": "low",
        },
    }

    message_log = log.splitlines()[-1].lower()
    for error in mapped_errors:
        error_name = error.lower()
        if message_log in error_name:
            return analyze_error(log)

    if not message_log or message_log not in mapped_errors:
        raise HTTPException(status_code=404, detail="Error not found")
