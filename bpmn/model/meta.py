

class BpmnModelMeta(type):

    def __new__(mcs, name, bases, dct):

        created = type.__new__(mcs, name, bases, dct)

        for ref_name, ref_type_name in dct.get('_%s__child_refs' % name, {}).items():
            def get_relevant_children(self):
                return self.children(ref_name)
            setattr(created, ref_name, property(get_relevant_children))

        return created

