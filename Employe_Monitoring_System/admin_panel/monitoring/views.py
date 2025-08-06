from django.shortcuts import render
from .models import ScreenshotLog
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def screenshot_log_view(request):
    username_filter = request.GET.get("username")
    date_filter = request.GET.get("date")

    logs = ScreenshotLog.objects.all().order_by('-timestamp')

    # Apply filters if provided
    if username_filter:
        logs = logs.filter(username=username_filter)

    if date_filter:
        logs = logs.filter(timestamp__date=date_filter)

    # Get all usernames for dropdown list
    usernames = ScreenshotLog.objects.values_list("username", flat=True).distinct()

    return render(request, 'monitoring/screenshot_log.html', {
        'logs': logs,
        'usernames': usernames,
        'selected_username': username_filter,
        'selected_date': date_filter
    })


@csrf_exempt
def upload_screenshot(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        timestamp = request.POST.get('timestamp')
        image_file = request.FILES.get('image')
        device_info = request.POST.get('data')
        ip=request.POST.get('ip')
        #user_agent = request.META.get('HTTP_USER_AGENT')

        if not username or not timestamp or not image_file:
            return JsonResponse({'error': 'Missing data'}, status=400)

        log = ScreenshotLog(
            username=username,
            timestamp=timestamp,
            image=image_file,
            ip_address=ip,
            device_info=device_info
        )
        log.save()

        return JsonResponse({'message': 'Screenshot uploaded successfully'})
    else:
        return JsonResponse({'error': 'Invalid Request'}, status=400)
