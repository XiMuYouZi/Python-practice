from django.template import Template, Context
from django.conf import settings
settings.configure()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.db import connection
cursor=connection.cursor()

# raw_template='''
# {% for object in objects %}
#     {% if forloop.first %}<li class="first">{% else %}<li>{% endif %}
#     {{ object }}
#     </li>
# {% endfor %}'''
#
# t=Template(raw_template)
# c=Context({'objects':['ws',1,(1,3,4),[1,'wew','we1']]})
# print t.render(c)
#
#
# person={'name':" NIKITA",'age':'12','location':'NewYork'}
# t=Template('{{person.name|max} is {{person.age}} years old, and her live at {{person.location}}')
# c= Context({'person':person})
# print t.render(c)
#
#
# t=Template('item is {{item.3}}')
# c=Context({'item':[2,3,4,1,8]})
# print t.render(c)
#
# t='''
# {%if athlete_list%}
#   <p>here are the athletes:{{athete_list}}.</p>
# {%else%}
#    <p>no athlets are available</p>
#    {%if coach_list%}
#      <p>here are the coaches:{{coach-list}}</p>
#    {%endif%}
# {%endif%}
# '''


