"""Define class for Skills Requirment argument."""
from args import _ArgType, _ARG_TYPE_TO_QUERY_KEY, _QueryValues, _QueryKVPairs
from args.meta_arg import MetaArg
from args.arg import Arg


class SkillsReq(Arg, metaclass=MetaArg, argtype=_ArgType._SKILLS_REQUIREMENT):
    """Skills Requirement argument."""
    _QUERY_KEY = _ARG_TYPE_TO_QUERY_KEY[_ArgType._OTHER_REQUIREMENT]

    @classmethod
    def _make_kvpairs(cls, query_values: _QueryValues) -> _QueryKVPairs:
        return {(cls._QUERY_KEY, (v,)) for v in query_values}
