from main.utils import HomeMixin, WorkMixin

class HomePlumbing(HomeMixin):
    template_name = 'main/plumbing_home.html'
    success_url = "/"
    service_type = 'plumbing'

class HomeElectricity(HomeMixin):
    template_name = 'main/electricity_home.html'
    success_url = "/electricity/"
    service_type = 'electricity'

class WorkPlumbing(WorkMixin):
    template_name = 'main/plumbing_work.html'
    success_url = "/"
    service_type = 'plumbing'

class WorkElectricity(WorkMixin):
    template_name = 'main/electricity_work.html'
    success_url = "/electricity/"
    service_type = 'electricity'

        
        