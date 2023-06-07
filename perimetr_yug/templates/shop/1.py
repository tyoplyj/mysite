<ul class="navbar-nav">
{% if cat_selected == 0 %}
    <li class="text-white nav-item selected">Все категории</li>
{% else %}
    <li class="text-white nav-item"><a class="nav-link text-white" href="{% url 'home' %}">Все категории</a></li>
{% endif %}

{% for c in cats %}
    {% if c.pk == cat_selected %}
        <li class="text-white nav-item selected">{{c.name}}</li>
    {% else %}
        <li class="nav-item"><a class="nav-link" href="{{ c.get_absolute_url }}">{{c.name}}</a></li>
    {% endif %}
{% endfor %}
</ul>