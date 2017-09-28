from django.shortcuts import render_to_response

import logging

def index(request):
    useragent_logger = logging.getLogger('useragent_logger')
    useragent_logger.debug(request.user_agent.browser)
    useragent_logger.debug(request.user_agent.os)
    useragent_logger.debug(request.user_agent.device)

    #IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')
    useragent_logger.debug("IP: "+ ipaddress)

    return render(request, 'principal/index.html', {})

