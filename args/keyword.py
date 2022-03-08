"""Define class for Keyword argument."""
from args import _ArgType, _QueryValues, _QueryKVPairs, _ARG_TYPE_TO_QUERY_KEY
from args.meta_arg import MetaArg
from args.arg import Arg


class Keyword(Arg, metaclass=MetaArg, argtype=_ArgType._KEYWORD):
    """Keyword argument."""
    
    @classmethod
    def _make_kvpairs(cls, query_values: _QueryValues) -> _QueryKVPairs:
        # keyword=v1+v2+...
        key = _ARG_TYPE_TO_QUERY_KEY[cls._ARGTYPE]
        return {(key, tuple([v for v in query_values]))}
