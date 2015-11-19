from django.utils.datastructures import MultiValueDict
import six

class MVD(MultiValueDict):

    def update(self, *args, **kwargs):
        if len(args) > 1:
            raise TypeError("update expected at most 1 arguments, got %d" % len(args))
        if args:
            other_dict = args[0]
            if isinstance(other_dict, MultiValueDict):
                for key, value_list in other_dict.lists():
                    self.setlistdefault(key).extend(value_list)
            else:
                try:
                    for key, value in other_dict.items():
                        if value != []:
                            a = self.setlistdefault(key)
                            if isinstance(value, list):
                                a += value
                            elif isinstance(value, int):
                                a.append(str(value))
                            else:
                                a.append(value)
                except TypeError:
                    raise ValueError("MultiValueDict.update() takes either a MultiValueDict or dictionary")
        for key, value in six.iteritems(kwargs):
            self.setlistdefault(key).append(value)
