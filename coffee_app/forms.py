from django import forms
from .models import BrewEntry
from .models import Roast

from django import forms
from .models import BrewEntry


class BrewEntryForm(forms.ModelForm):
    class Meta: #meta data controls the form without a field
        model = BrewEntry
        fields = [
            "title",
            "roast",
            "brew_method",
            "other_brew_method",
            "entry",
            "rating",
        ]
        widgets = {
            "entry": forms.Textarea(attrs={"rows": 4}), #UI
        }

    def clean(self):
        cleaned_data = super().clean()
        brew_method = cleaned_data.get("brew_method")
        other_method = cleaned_data.get("other_brew_method")

        if brew_method == "other" and not other_method:
            self.add_error(
                "other_brew_method",
                "Please specify the brew method if you select 'Other'."
            )

        return cleaned_data



