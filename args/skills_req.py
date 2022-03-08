"""Define class for Skills Requirment argument."""
from args import _ArgType
from args.meta_arg import MetaArg
from args.arg import Arg


class SkillsReq(Arg, metaclass=MetaArg, argtype=_ArgType._SKILLS_REQUIREMENT):
    """Skills Requirement argument."""

    pass  # Default good
