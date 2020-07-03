from django import forms


class Inserting_data(forms.Form):

    movie_id = forms.IntegerField(
        label='Enter movie ID',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'movie id'
            }
        )
    )
    movie_name = forms.CharField(
        label='Enter Movie Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Movie_name'
            }
        )
    )
    timings = forms.TimeField(
        label='Enter Movie Timings',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Timings'
            }
        )
    )
    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }
        )
    )


class Updating_data(forms.Form):

    movie_id = forms.IntegerField(
        label='Enter movie ID',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'movie id'
            }
        )
    )
    movie_name = forms.CharField(
        label='Enter Movie Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Movie_name'
            }
        )
    )
    timings = forms.TimeField(
        label='Enter Movie Timings',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Timings'
            }
        )
    )
    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }
        )
    )


class deleting_data(forms.Form):

    movie_id = forms.IntegerField(
        label='Enter movie ID',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'movie id'
            }
        )
    )
    movie_name = forms.CharField(
        label='Enter Movie Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Movie_name'
            }
        )
    )
