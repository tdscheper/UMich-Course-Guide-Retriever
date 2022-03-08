"""Define class that holds all Course Guide arguments."""
from args import _ArgType, _NUM_STANDALONE_ARGTYPES, _INPUT_KEY_TO_ARG_TYPE, \
                 _InputKey, _RawInputValue, _InputValue, \
                 _ARG_TYPE_TO_DEFAULT_INPUT_VALUE
from args.argtype_to_arg import ARGTYPE_TO_ARG
from args.arg import Arg
from typing import Dict, Optional, Type


class CGArgs:
    """All Course Guide arguments."""

    def __init__(self) -> None:
        self.args: Dict[Type[_ArgType], Optional[Arg]] = {
            _ArgType(i): None for i in range(1, _NUM_STANDALONE_ARGTYPES + 1)
        }
        self.set_show()
    
    def add_arg(self, argtypestr: _InputKey, input: _RawInputValue) -> None:
        self._set_arg(_INPUT_KEY_TO_ARG_TYPE[argtypestr], input)
    
    def set_show(self, value: Optional[_InputValue] = None):
        if value is None:
            value = _ARG_TYPE_TO_DEFAULT_INPUT_VALUE[_ArgType._SHOW]
        self._set_arg(_ArgType._SHOW, value)
    
    def get_show_int(self) -> int:
        # Show should only ever have one QueryKVPair, so just pop it off,
        # grab the value, add it back, and then return the value
        # Have to do this since sets are not subscriptable
        kvpair = self.args[_ArgType._SHOW].kvpairs.pop()
        show_int = int(kvpair[1][0])
        self.args[_ArgType._SHOW].kvpairs.add(kvpair)
        return show_int
    
    def url_piece(self) -> str:
        piece = ''
        for _, arg in self.args.items():
            if arg is not None:
                piece += arg.url_piece() + '&'
        return piece[:-1]  # Remove last &
    
    def _set_arg(self, argtype: Type[_ArgType], input: _RawInputValue) -> None:
        self.args[argtype] = ARGTYPE_TO_ARG[argtype](input)
