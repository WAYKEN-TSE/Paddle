
# This file is generated by PaConvert ToolKit, please Don't edit it!
import paddle

def reshape(self, *args, **kwargs):
    if args:
        if len(args)==1 and isinstance(args[0], (tuple, list)):
            return paddle.reshape(self, args[0])
        else:
            return paddle.reshape(self, list(args))
    elif kwargs:
        assert 'shape' in kwargs
        return paddle.reshape(self, shape=kwargs['shape'])

setattr(paddle.Tensor, 'reshape', reshape)
