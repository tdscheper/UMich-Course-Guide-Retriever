"""Define class for Instruction Mode argument."""
from args import _ArgType
from args.meta_arg import MetaArg
from args.arg import Arg


class InstructionMode(Arg, metaclass=MetaArg, 
                      argtype=_ArgType._INSTRUCTION_MODE):
    """Instruction Mode argument."""

    pass  # Default good
