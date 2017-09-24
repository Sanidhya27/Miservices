from django import forms

class ServiceRequest(forms.Form):
	
    QuantityName=forms.CharField(label='Quantity Name')
    QuantityDemanded=forms.IntegerField(label='Quantity Demanded')
    QuantitySupplied=forms.IntegerField(label='Quantity Supplied')
    Demandedby=forms.CharField(label='Department')