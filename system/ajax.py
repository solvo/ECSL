# -*- coding: utf-8 -*-
from system.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseBadRequest


@login_required()
def profileAddLike(request):
    profile = request.user.profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.likes.add(speech)
    print(Profile.objects.filter(likes=idSpeech).count())
    return JsonResponse({'messages': Profile.objects.filter(likes=idSpeech).count()})


@login_required()
def matricularse(request):
    profile = request.user.profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.matriculatedspeechs.add(speech)
    return JsonResponse({'messages': "Matricula confirmada"})


@login_required()
def deleteMatricularse(request):
    profile = request.user.profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.matriculatedspeechs.remove(speech)
    return JsonResponse({'mensaje': "Matricula eliminada"})


@login_required()
def deleteRecurso(request):
    user = request.user
    idRecurso = request.POST['id_recurso']
    recurso = get_object_or_404(SpeechResource, pk=idRecurso)
    if user != recurso.speech.user:
        return HttpResponseBadRequest()
    else:
        recurso.recurso.delete()
        recurso.delete()
    return JsonResponse({'mensaje': "Recurso eliminado"})
