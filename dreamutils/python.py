#!/usr/bin/python3

import ast as _ast
from types import FunctionType as _FunctionType, ModuleType as _ModuleType, MethodType as _MethodType
from typing import Dict as _Dict, List as _List, Union as _Union

"""This file contains utils to analyze and manipulate raw python files"""


def class_of_method(method: _MethodType) -> _Union[None, type]:
    """
    Returns the class in which the given `method` was defined

    Args:
        method (method): Method from which you want to find out from which class it was declared

    Returns:
        The class where the method was defined or None

    """
    method_name = method.__name__
    if method.__self__:
        classes = [method.__self__.__class__]
    else:
        classes = [method.im_class]
    while classes:
        c = classes.pop()
        if method_name in c.__dict__:
            return c
        else:
            classes = list(c.__bases__) + classes
    return None


def defined_functions_and_classes(file_or_module: _Union[str, _ModuleType], include_external_modules=False) -> _Dict[str, _Union[_FunctionType, type, _ModuleType]]:
    """
    Returns all functions and classes from a given python file or python module

    Args:
        file_or_module (str or ModuleType): The file or module from which you want to get the functions and classes.
        include_external_modules (bool): If True the modules, functions and classes which were imported are getting returned too.

    Returns:
        dict: A dict of str - function, class or module pairs with all functions, classes and modules -> (if `include_external_modules` is True).

    Notes:
        If `file_or_module` is a file the returned dict values will all be None

    """
    functions_and_classes = {}
    if isinstance(file_or_module, str):
        with open(file_or_module, "r") as file:
            parsed = _ast.parse(file.read(), filename=file_or_module)
            for x in parsed.body:
                if isinstance(x, (_ast.FunctionDef, _ast.ClassDef, _ModuleType)):
                    functions_and_classes[x.name] = None
            file.close()
    elif isinstance(file_or_module, _ModuleType):
        for x in dir(file_or_module):
            functions_and_classes[x] = getattr(file_or_module, x)

    if not include_external_modules:
        for name, module_type in functions_and_classes.copy().items():
            try:
                if isinstance(module_type, _ModuleType):
                    del functions_and_classes[name]
            except:
                pass

    return functions_and_classes


def extract_decorated_func(function: _FunctionType) -> _FunctionType:
    """
    Extracts the 'core' function of a function which has decorators.
    When a function with decorators is called, the decorators are called first and then the function.
    This is good to see when `print(function_with_decorator)` is called, then the decorator object gets printed out instead of the function object.

    Note:
        This method only works properly if every decorator calls the function normally (function_name()).

    Args:
        function (FunctionType): Function which should be extracted.

    Returns:
        FunctionType: The extracted function.

    """
    function_types = []

    try:
        for x in function.__closure__:
            function_types.append(x.cell_contents)
    except TypeError:
        return function

    while len(function_types) > 0:
        for func in function_types.copy():
            if isinstance(func, _FunctionType):
                try:
                    for x in func.__closure__:
                        function_types.append(x.cell_contents)
                except TypeError:
                    return func


def get_decorators(function: _FunctionType) -> _List[_FunctionType]:
    """
    Returns all decorators of a function

    Note:
        This method only works properly if every decorator calls the function normally (function_name()).

    Args:
        function (FunctionType): Function from which the decorators should be extracted from.

    Returns:
        list: A list of the function decorators

    """
    decorators = []
    function_types = []
    try:
        for x in function.__closure__:
            function_types.append(x.cell_contents)
        decorators.append(function)
    except TypeError:
        return []

    while len(function_types) > 0:
        for func in function_types:
            if isinstance(func, _FunctionType):
                decorators.append(func)
                try:
                    for z in func.__closure__:
                        function_types.append(z.cell_contents)
                except TypeError:
                    pass
            function_types.remove(func)

    return decorators[:-1]
