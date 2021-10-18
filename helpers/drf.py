class GenericSerializerClass:
    def get_serializer_class(self):
        if hasattr(self.action, "list"):
            return getattr(self, self.action)

        return self.serializer_class
