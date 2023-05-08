import dtlpy as dl;
# dl.setenv("rc")
dl.login_m2m(email=<YOUR_EMAIL>, password=<YOUR_PASSWORD>)
project = dl.projects.get(project_id='9ec27f9f-1b89-4b9c-adcf-1fb610a443cf')
project.print()
bot = project.bots.create(name='audio-application-bot', return_credentials=True)
bot.print()