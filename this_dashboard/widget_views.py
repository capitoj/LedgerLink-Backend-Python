import datetime

#import MySQLdb
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.response import TemplateResponse

from xf.uc_dashboards.views import WidgetView
from django.conf import settings



def widget_blank(request):
    c = {'current_time': 'here we go',}

    return TemplateResponse(request, 'widgets/w_blank.html', c)

def widget_current_time(request):
    c = {'current_time': datetime.datetime.now()}

    return TemplateResponse(request, 'widgets/w_current_time.html', c)

def widget_preterm_tiles(request):
    return TemplateResponse(request, 'widgets/w_preterm_tiles.html')


########################################################################################################################
class PTBIWidgetView(WidgetView):
    """
    Serves as a base class for all PTBI-based widgets.
    """

    def get_connection(self):
        """
        Returns a connection object for PTBi
        :return: The connection object
        """

        conn = MySQLdb.connect(settings.DATABASES["ptbi_data"]["HOST"],
                               settings.DATABASES["ptbi_data"]["USER"],
                               settings.DATABASES["ptbi_data"]["PASSWORD"],
                               settings.DATABASES["ptbi_data"]["NAME"],
                               int(settings.DATABASES["ptbi_data"]["PORT"]))

        return conn

########################################################################################################################
class WCurrentTime(PTBIWidgetView):
    template_name = "widgets/w_current_time.html"

    def get_context_data(self, **kwargs):
        context = super(WCurrentTime, self).get_context_data(**kwargs)
        context["current_time"] = datetime.datetime.now()

        return context

########################################################################################################################
class WDiagnosisList(PTBIWidgetView):
    template_name = "generic_widgets/w_table.html"

    def get_context_data(self, **kwargs):
        context = super(WDiagnosisList, self).get_context_data(**kwargs)

        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(" SELECT final_diagnosis, COUNT(final_diagnosis) as number " \
                            "FROM uganda_facility_register_data " \
                            "GROUP BY final_diagnosis " \
                            "ORDER BY final_diagnosis ")
            rows = cursor.fetchall()
        finally:
            conn.close()

        context["caption"] = "Diagnosis counts"
        self.data_columns.append(('Final diagnosis', '70%', 'final_diagnosis'))
        self.data_columns.append(('Number', '30%', 'number'))
        rows = self.result_set_to_dict(rows, ['final_diagnosis', 'number'])
        context["rows"] = rows;
        return context


########################################################################################################################
class WDiagnosisPie(PTBIWidgetView):
    """
    This widget generates a pie chart. It uses a generic widget template, pie. Documented example
    """

    #The name of the template. This is what will be rendered. For this purpose, a generic pie is sufficient.
    template_name = "generic_widgets/w_pie.html"

    #This method returns a context. It is the right place to set any data that you want to display in the
    #template.
    def get_context_data(self, **kwargs):

        #Always call the super method, this will initialise this class and do some work behind the scenes.
        context = super(WDiagnosisPie, self).get_context_data(**kwargs)

        #Get connection lives in PTBIWigdetView and creates a connection object
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(" SELECT final_diagnosis, COUNT(final_diagnosis) as number " \
                            "FROM uganda_facility_register_data " \
                            "GROUP BY final_diagnosis " \
                            "ORDER BY final_diagnosis ")
            rows = cursor.fetchall()
        finally:
            conn.close()

        #Set the caption of the widgets
        context["caption"] = "Diagnoses"

        #Fill the data table
        self.data_columns.append(('Final diagnosis', '70%', 'final_diagnosis'))
        self.data_columns.append(('Number', '30%', 'number'))

        #Convert the record result set to a list of dictionaries, which can then be used in the template
        rows = self.result_set_to_dict(rows, ['final_diagnosis', 'number'])

        #If you want to loop through rows in the template, create a rows context variable. Not needed in the pie
        #though.
        context["rows"] = rows;

        #Create an emptry array for the labels, and load it from the rows. The labels appear in the pie chart
        labels = []
        for row in rows:
            labels.append(row['final_diagnosis'])
        #Assign the array to the labels context variable, which will be injected into the JavaScript in the
        #template
        context["labels"] = str(labels).replace("'", '"')

        #Create an empty array of data points, and fill it and asign it to a context variable. It will be inserted
        #into the javascript on the template
        datapoints = []
        for row in rows:
            datapoints.append(str(row['number']))
        context["datapoints"] = str(datapoints).replace("'", '')

        #This text will appear below the caption
        context["extra_text"] = "Showing diagnoses in Uganda"

        return context

    pass


########################################################################################################################
class WModesOfDeliveryPie(PTBIWidgetView):
    template_name = "generic_widgets/w_pie.html"

    def get_context_data(self, **kwargs):
        context = super(WModesOfDeliveryPie, self).get_context_data(**kwargs)

        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(" SELECT mode_of_delivery, COUNT(mode_of_delivery) as number " \
                            "FROM uganda_facility_register_data " \
                            "GROUP BY mode_of_delivery " \
                            "ORDER BY mode_of_delivery ")
            rows = cursor.fetchall()
        finally:
            conn.close()

        self.data_columns.append(('Mode of delivery', '70%', 'mode_of_delivery'))
        self.data_columns.append(('Number', '30%', 'number'))

        context["caption"] = "Modes of delivery"
        rows = self.result_set_to_dict(rows, ['mode_of_delivery', 'number'])
        context["rows"] = rows;
        labels = []
        for row in rows:
            labels.append(row['mode_of_delivery'])
        context["labels"] = str(labels).replace("'", '"')

        datapoints = []
        for row in rows:
            datapoints.append(str(row['number']))
        context["datapoints"] = str(datapoints).replace("'", '')
        context["extra_text"] = "Showing the various modes of delivery in Uganda."

        return context

    pass


