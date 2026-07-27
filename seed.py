# Script para popular o banco com os erros conhecidos
# Execute: python seed.py
import asyncio

from database.database import async_session_maker
from models.known_error import KnownError


async def main():
    mapped_errors = {
        # --- Erros Aritméticos ---
        "ZeroDivisionError": {
            "summary": "Raised when a number is divided by zero, either using the division operator (/) or the modulo operator (%).",
        },
        "OverflowError": {
            "summary": "Raised when the result of an arithmetic operation exceeds the maximum limit representable by the numeric type.",
        },
        "FloatingPointError": {
            "summary": "Raised when a floating-point operation fails, typically when floating-point exception handling is enabled.",
        },
        # --- Erros de Tipo e Valor ---
        "TypeError": {
            "summary": "Raised when an operation or function is applied to an object of an unsuitable type, such as adding a string to an integer.",
        },
        "ValueError": {
            "summary": "Raised when a function receives an argument of the correct type but with an inappropriate value, such as int('abc').",
        },
        "AssertionError": {
            "summary": "Raised when an assert statement evaluates to False, commonly used for debugging and testing assumptions.",
        },
        # --- Erros de Estrutura de Dados ---
        "IndexError": {
            "summary": "Raised when attempting to access an index that is out of range in a list, tuple, or other sequence.",
        },
        "KeyError": {
            "summary": "Raised when a dictionary is accessed with a key that does not exist in it.",
        },
        "AttributeError": {
            "summary": "Raised when an attribute is accessed or assigned on an object that does not support it.",
        },
        "StopIteration": {
            "summary": "Raised by the next() function when an iterator has no more items to return.",
        },
        "StopAsyncIteration": {
            "summary": "Raised by an asynchronous iterator's __anext__() method when there are no further items to produce.",
        },
        # --- Erros de Nome e Escopo ---
        "NameError": {
            "summary": "Raised when a variable or name is referenced before being defined or is not found in the current scope.",
        },
        "UnboundLocalError": {
            "summary": "Raised when a local variable is referenced inside a function before being assigned a value.",
        },
        # --- Erros de Importação e Módulo ---
        "ImportError": {
            "summary": "Raised when an import statement fails, either because the module doesn't exist or because something inside it couldn't be loaded.",
        },
        "ModuleNotFoundError": {
            "summary": "A subclass of ImportError, raised specifically when the module being imported cannot be found.",
        },
        # --- Erros de Sistema e Memória ---
        "MemoryError": {
            "summary": "Raised when an operation fails because the interpreter runs out of available memory.",
        },
        "RecursionError": {
            "summary": "Raised when the maximum recursion depth is exceeded, usually caused by infinite or deeply nested recursive calls.",
        },
        "SystemError": {
            "summary": "Raised when the Python interpreter encounters an internal error that is not serious enough to cause it to abort.",
        },
        "RuntimeError": {
            "summary": "Raised when an error occurs that doesn't fit into any other specific category.",
        },
        "NotImplementedError": {
            "summary": "Raised inside abstract methods or stubs to indicate that a subclass must provide a concrete implementation.",
        },
        # --- Erros de Sintaxe e Indentação ---
        "SyntaxError": {
            "summary": "Raised when Python encounters code that does not follow the language's grammar rules and cannot be parsed.",
        },
        "IndentationError": {
            "summary": "Raised when the indentation of a code block is incorrect or inconsistent.",
        },
        "TabError": {
            "summary": "A subclass of IndentationError, raised when tabs and spaces are mixed in an inconsistent way for indentation.",
        },
        # --- Erros de Arquivo e Sistema Operacional ---
        "OSError": {
            "summary": "Raised when a system-level operation fails, such as reading a file, accessing a network, or calling an OS function.",
        },
        "FileNotFoundError": {
            "summary": "Raised when a file or directory is requested but cannot be found at the specified path.",
        },
        "FileExistsError": {
            "summary": "Raised when attempting to create a file or directory that already exists.",
        },
        "PermissionError": {
            "summary": "Raised when an operation is attempted without the required system permissions, such as writing to a read-only file.",
        },
        "IsADirectoryError": {
            "summary": "Raised when a file operation (like read or write) is performed on a path that points to a directory instead of a file.",
        },
        "NotADirectoryError": {
            "summary": "Raised when a directory operation is attempted on a path that is not a directory.",
        },
        "TimeoutError": {
            "summary": "Raised when a system function or operation exceeds the allowed time limit.",
        },
        "BlockingIOError": {
            "summary": "Raised when an I/O operation would block on an object set for non-blocking mode.",
        },
        "ChildProcessError": {
            "summary": "Raised when an operation on a child process fails.",
        },
        "BrokenPipeError": {
            "summary": "Raised when writing to a pipe or socket that has been closed by the other end.",
        },
        "ConnectionError": {
            "summary": "A base class for connection-related errors, raised when a network connection fails or is interrupted.",
        },
        "ConnectionAbortedError": {
            "summary": "Raised when a network connection attempt is aborted by the remote host.",
        },
        "ConnectionRefusedError": {
            "summary": "Raised when a network connection attempt is actively refused by the target machine.",
        },
        "ConnectionResetError": {
            "summary": "Raised when a network connection is forcibly closed by the remote peer.",
        },
        "InterruptedError": {
            "summary": "Raised when a system call is interrupted by an external signal before it could complete.",
        },
        "ProcessLookupError": {
            "summary": "Raised when a process with the given ID does not exist.",
        },
        # --- Erros de Unicode e Encoding ---
        "UnicodeError": {
            "summary": "Base class for encoding and decoding errors related to Unicode text handling.",
        },
        "UnicodeDecodeError": {
            "summary": "Raised when a byte sequence cannot be decoded into a string using the specified encoding.",
        },
        "UnicodeEncodeError": {
            "summary": "Raised when a string character cannot be encoded into bytes using the specified encoding.",
        },
        "UnicodeTranslateError": {
            "summary": "Raised when a character cannot be translated during a Unicode string translation operation.",
        },
        "ReferenceError": {
            "summary": "Raised when a weak reference proxy is used to access an object that has already been garbage collected.",
        },
        "BufferError": {
            "summary": "Raised when an operation related to a buffer object cannot be performed.",
        },
        "EOFError": {
            "summary": "Raised when the input() function reaches the end of a file without reading any data.",
        },
        "Warning": {
            "summary": "Base class for all warning categories in Python.",
        },
        "DeprecationWarning": {
            "summary": "Issued when a feature or behavior is deprecated and may be removed in a future version of Python.",
        },
        "UserWarning": {
            "summary": "The default warning category used when calling warnings.warn() without specifying a type.",
        },
        "FutureWarning": {
            "summary": "Issued when a behavior will change in a future version of Python, aimed at end users.",
        },
        "RuntimeWarning": {
            "summary": "Issued when a suspicious runtime behavior is detected, such as invalid floating-point operations.",
        },
        "SyntaxWarning": {
            "summary": "Issued when Python detects a questionable syntax that is technically valid but potentially problematic.",
        },
        "ResourceWarning": {
            "summary": "Issued when a resource such as a file or network connection is not properly closed.",
        },
        "PendingDeprecationWarning": {
            "summary": "Issued when a feature is considered for deprecation but has not been officially deprecated yet.",
        },
        "ImportWarning": {
            "summary": "Issued when an import operation triggers something that could indicate a problem or unusual behavior.",
        },
        "UnicodeWarning": {
            "summary": "Issued when a Unicode-related conversion or comparison may produce unexpected results.",
        },
        "BytesWarning": {
            "summary": "Issued when bytes or bytearray objects are compared with strings, which may indicate a logic error.",
        },
        "EncodingWarning": {
            "summary": "Issued when an encoding is not explicitly specified in operations that deal with text files.",
        },
                "ArithmeticError": {
            "summary": "Base class for errors that occur during numeric calculations, such as ZeroDivisionError, OverflowError, and FloatingPointError.",
        },
        "LookupError": {
            "summary": "Base class for errors raised when a key or index used to look up a value is invalid, such as IndexError and KeyError.",
        },
        "SystemExit": {
            "summary": "Raised by the sys.exit() function to request termination of the program; not a typical error, but often appears in tracebacks.",
        },
        "KeyboardInterrupt": {
            "summary": "Raised when the user interrupts program execution, usually by pressing Ctrl+C.",
        },
        "GeneratorExit": {
            "summary": "Raised inside a generator or coroutine when its close() method is called to request termination.",
        },
        "ExceptionGroup": {
            "summary": "Raised to bundle multiple unrelated exceptions together, typically handled using the except* syntax introduced in Python 3.11.",
        },
        "BaseExceptionGroup": {
            "summary": "The base class for ExceptionGroup, used to wrap multiple BaseException instances, including those that are not standard Exception subclasses.",
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
