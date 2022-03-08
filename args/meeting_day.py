"""Define class for Meeting Day argument."""
from args import _ArgType, _QueryValues, _QueryKVPairs, _ARG_TYPE_TO_QUERY_KEY
from args.meta_arg import MetaArg
from args.arg import Arg


class MeetingDay(Arg, metaclass=MetaArg, argtype=_ArgType._MEETING_DAY):
    """Meeting Day argument."""

    @classmethod
    def _make_kvpairs(cls, query_values: _QueryValues) -> _QueryKVPairs:
        key = _ARG_TYPE_TO_QUERY_KEY[cls._ARGTYPE]
        return {(key, tuple([','.join(query_values)]))}
    