.. _{{ fullname }}:

.. raw:: html

    <br>

.. image:: skulllinesmall3.jpg
    :width: 100%
    :height: 2.2cm
    :target: index.html


.. raw:: html

    <br><br><center><i>Prosecutor. Reconsider. OTP-CR-117/19.</i></center><br><br>


{{ fullname }}
{{ underline }}

.. raw:: html

    <br>

.. automodule:: {{ fullname }}
    :members:

    {% block exceptions %}
    {% if exceptions %}
    .. rubric:: exceptions

    .. autosummary::
    {% for item in exceptions %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block classes %}
    {% if classes %}
    .. rubric:: classes

    .. autosummary:: 
    {% for item in classes %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block functions %}
    {% if functions %}
    .. rubric:: functions

    .. autosummary::
    {% for item in functions %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    .. raw:: html

        <br><br>
