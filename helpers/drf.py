from rest_framework.viewsets import ViewSetMixin


class GenericSerializerClass(ViewSetMixin):
    def get_serializer_class(self):
        serializer_class_name = f"{self.action}_serializer_class"
        serializer_class = getattr(self, serializer_class_name, None)

        return serializer_class if serializer_class else self.serializer_class
