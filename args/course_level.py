"""Define a class for Course Level argument."""
from args import _ArgType
from args.meta_arg import MetaArg
from args.arg import Arg


class CourseLevel(Arg, metaclass=MetaArg, argtype=_ArgType._COURSE_LEVEL):
    """Course Level argument."""

    pass  # Default good
