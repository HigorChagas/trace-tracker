# Script para popular o banco com os erros conhecidos
# Execute: python seed.py
import asyncio

from database.database import async_session_maker
from models.known_error import KnownError


async def main():
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
        "IndexError: list index out of range": {
            "summary": "occurs when you try to access an index that doesn't exist in a list or sequence.",
        },
        "KeyError": {
            "summary": "raised when a dictionary key is not found.",
        },
        "AttributeError": {
            "summary": "raised when an attribute reference or assignment fails on an object.",
        },
        "FileNotFoundError": {
            "summary": "raised when a file or directory is requested but doesn't exist.",
        },
        "ImportError": {
            "summary": "raised when an import statement fails to find the module.",
        },
        "NameError": {
            "summary": "raised when a local or global name is not found.",
        },
        "RecursionError": {
            "summary": "raised when the maximum recursion depth is exceeded.",
        },
        "MemoryError": {
            "summary": "raised when an operation runs out of memory.",
        },
    }
    async with async_session_maker() as session:
        for error in mapped_errors:
            known_errors = KnownError(
                error_name=error,
                summary=mapped_errors[error]["summary"],
                language="Python",
            )
            session.add(known_errors)
        await session.commit()


asyncio.run(main())
