from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from usuario.models import CustomUsuario


class CustomUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ['nome', 'sobrenome', 'celular']
        # labels = {'username': 'username'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ('nome', 'sobrenome', 'celular')
