import click

countOutput = [click.option("--countOutput", "-c", "countOutput", is_flag=True, help="Return count of objects instead of data.")]
limit = [click.option("--limit", "-l", "limit", type=int, default=1000, help="Limit results returned.")]
eventid_from = [click.option("--eventid_from", "eventid_from", type=int, help="Return only objects equal to or less than event id.")]
eventid_till = [click.option("--eventid_till", "eventid_till", type=int, help="Return only objects equal to or more than event id.")]
problem_time_from = [click.option("--problem_time_from", "problem_time_from", help="Return only objects that were in the problem state starting with problem_time_from. Applies only if the source is trigger event and object is trigger. Mandatory if problem_time_till is specified.")]
problem_time_till = [click.option("--problem_time_till", "problem_time_till", help="Return only objects that were in the problem state until problem_time_till. Applies only if the source is trigger event and object is trigger. Mandatory if problem_time_from is specified.")]
time_from = [click.option("--time_from", "time_from", help="Return only objects that have been generated after the given time")]
time_till = [click.option("--time_till", "time_till", help="Return only objects that have been generated before the given time.")]
intervals_from = [click.option("--intervals_from", "intervals_from", help="Time intervals to return service layer availability information about")]
intervals_to = [click.option("--intervals_to", "intervals_to", help="Time intervals to return service layer availability information about")]
intervals = [click.option("--intervals", "intervals", help="Time intervals to return service layer availability information about")]
lastChangeSince = [click.option("--lastChangeSince", "lastChangeSince", help="Return only triggers that have changed their state after the given time.")]
lastChangeTill = [click.option("--lastChangeTill", "lastChangeTill", help="Return only triggers that have changed their state before the given time.")]
acknowledged = [click.option("--acknowledged", "acknowledged", is_flag=True, help="Return objects that have been acknowledged.")]
active = [click.option("--active", "active", is_flag=True, help="enabled triggers that belong to monitored hosts.")]
dependent = [click.option("--dependent", "dependent", is_flag=True, help="objects with triggers that have dependencies")]
editable = [click.option("--editable", "editable", is_flag=True, help="objects with write permissions.")]
excludeSearch = [click.option("--excludeSearch", "excludeSearch", is_flag=True, help="results that do not match the search criteria.")]
expandComment = [click.option("--expandComment", "expandComment", is_flag=True, help="Expand macros in the trigger description.")]
expandDescription = [click.option("--expandDescription", "expandDescription", is_flag=True, help="Expand macros in the name of the trigger.")]
expandExpression = [click.option("--expandExpression", "expandExpression", is_flag=True, help="Expand functions and macros in the trigger expression.")]
expandName = [click.option("--expandName", "expandName", is_flag=True, help="Expand macros in the name.")]
expandStepName = [click.option("--expandStepName", "expandStepName", is_flag=True, help="Expand macros in the names of steps.")]
expandUrls = [click.option("--expandUrls", "expandUrls", is_flag=True, help="Adds global map URLs to the corresponding map elements and expands macros in all map element URLs.")]
getAccess = [click.option("--getAccess", "getAccess", is_flag=True, help="Return user groups that the user belongs to in the usrgrps property.")]
globalmacro = [click.option("--globalmacro", "globalmacro", is_flag=True, help="Return global macros instead of host macros.")]
inherited = [click.option("--inherited", "inherited", is_flag=True, help="Return objects that have been inherited.")]
maintenance = [click.option("--maintenance", "maintenance", is_flag=True, help="Return enabled triggers that belong to hosts in maintenance")]
monitored = [click.option("--monitored", "monitored", is_flag=True, help="Return enabled objects that belong to monitored host.")]
monitored_hosts = [click.option("--monitored_hosts", "monitored_hosts", is_flag=True, help="Return objects that contain monitored hosts.")]
noInheritance = [click.option("--noInheritance", "noInheritance", is_flag=True, help="Do not return inherited template screens.")]
only_true = [click.option("--only_true", "only_true", is_flag=True, help="Return only triggers that have recently been in a problem state.")]
preservekeys = [click.option("--preservekeys", "preservekeys", is_flag=True, help="Use IDs as keys in the resulting array.")]
proxy_hosts = [click.option("--proxy_hosts", "proxy_hosts", is_flag=True, help="Return only objects that are proxies.")]
real_hosts = [click.option("--real_hosts", "real_hosts", is_flag=True, help="Return only objects that contain hosts.")]
templated = [click.option("--templated", "templated", is_flag=True, help="Return only objects that belong to a template.")]
templated_hosts = [click.option("--templated_hosts", "templated_hosts", is_flag=True, help="Return only objects that are templates.")]
webitems = [click.option("--webitems", "webitems", is_flag=True, help="Include web items in the result.")]
withAcknowledgedEvents = [click.option("--withAcknowledgedEvents", "withAcknowledgedEvents", is_flag=True, help="Return only objects with acknowledged events")]
withInventory = [click.option("--withInventory", "withInventory", is_flag=True, help="Return only objects with inventory data.")]
withLastEventUnacknowledged = [click.option("--withLastEventUnacknowledged", "withLastEventUnacknowledged", is_flag=True, help="Return only objects with last event unacknowledged")]
withUnacknowledgedEvents = [click.option("--withUnacknowledgedEvents", "withUnacknowledgedEvents", is_flag=True, help="Return only objects with unacknowledged events.")]
with_applications = [click.option("--with_applications", "with_applications", is_flag=True, help="Return only objects with applications.")]
with_graph_prototypes = [click.option("--with_graph_prototypes", "with_graph_prototypes", is_flag=True, help="Return only objects with graph prototypes.")]
with_graphs = [click.option("--with_graphs", "with_graphs", is_flag=True, help="Return only objects with graphs.")]
with_hosts_and_templates = [click.option("--with_hosts_and_templates", "with_hosts_and_templates", is_flag=True, help="Return only objects with hosts or templates.")]
with_httptests = [click.option("--with_httptests", "with_httptests", is_flag=True, help="Return only objects with http checks.")]
with_item_prototypes = [click.option("--with_item_prototypes", "with_item_prototypes", is_flag=True, help="Return only objects with item prototypes.")]
with_items = [click.option("--with_items", "with_items", is_flag=True, help="Return only objects hosts or templates with items todo.")]
with_monitored_httptests = [click.option("--with_monitored_httptests", "with_monitored_httptests", is_flag=True, help="Return only objects with enabled web checks.")]
with_monitored_items = [click.option("--with_monitored_items", "with_monitored_items", is_flag=True, help="Return only objects with enabled items.")]
with_monitored_triggers = [click.option("--with_monitored_triggers", "with_monitored_triggers", is_flag=True, help="Return only objects with enabled triggers.")]
with_simple_graph_item_prototypes = [click.option("--with_simple_graph_item_prototypes", "with_simple_graph_item_prototypes", is_flag=True, help="Return only objects item prototypes, which are enabled for creation and have numeric type of information.")]
with_simple_graph_items = [click.option("--with_simple_graph_items", "with_simple_graph_items", is_flag=True, help="Return only objects with numeric items.")]
with_triggers = [click.option("--with_triggers", "with_triggers", is_flag=True, help="Return only objects with triggers.")]
with_gui_access = [click.option("--with_gui_access", "with_gui_access", type=int, multiple=True, help="Return only objects with gui_access.")]
output = [click.option("--output", "output", multiple=True, metavar="PROPERTY", help="Object properties to be returned (refered to as 'output' in API docs).")]
selectFilter = [click.option("--selectFilter", "selectFilter", multiple=True, metavar="PROPERTY", help="Returns the action filter in the filter property.")]
selectOperations = [click.option("--selectOperations", "selectOperations", multiple=True, metavar="PROPERTY", help="Return action operations in the operations property.")]
selectRecoveryOperations = [click.option("--selectRecoveryOperations", "selectRecoveryOperations", multiple=True, metavar="PROPERTY", help="Returns the action filter in the filter property.")]
selectHosts = [click.option("--selectHosts", "selectHosts", multiple=True, metavar="PROPERTY", help="Returns the action filter in the filter property.")]
selectMediatypes = [click.option("--selectMediatypes", "selectMediatypes", multiple=True, metavar="PROPERTY", help="Returns the action filter in the filter property.")]
selectUsers = [click.option("--selectUsers", "selectUsers", multiple=True, metavar="PROPERTY", help="Returns the action filter in the filter property.")]
selectHost = [click.option("--selectHost", "selectHost", multiple=True, metavar="PROPERTY", help="Returns the filter in the filter property.")]
selectItems = [click.option("--selectItems", "selectItems", multiple=True, metavar="PROPERTY", help="Returns the action filter in the filter property.")]
selectDiscoveryRule = [click.option("--selectDiscoveryRule", "selectDiscoveryRule", multiple=True, metavar="PROPERTY", help="Returns the filter in the filter property.")]
selectApplicationDiscovery = [click.option("--selectApplicationDiscovery", "selectApplicationDiscovery", multiple=True, metavar="PROPERTY", help="Returns the filter in the filter property.")]
selectWidgets = [click.option("--selectWidgets", "selectWidgets", multiple=True, metavar="PROPERTY", help="Returns the action filter in the filter property.")]
selectUserGroups = [click.option("--selectUserGroups", "selectUserGroups", multiple=True, metavar="PROPERTY", help="Returns the action filter in the filter property.")]
selectDRules = [click.option("--selectDRules", "selectDRules", multiple=True, metavar="PROPERTY", help="Returns the filter in the filter property.")]
selectDServices = [click.option("--selectDServices", "selectDServices", multiple=True, metavar="PROPERTY", help="Returns the filter in the filter property.")]
selectDHosts = [click.option("--selectDHosts", "selectDHosts", multiple=True, metavar="PROPERTY", help="Returns the filter in the filter property.")]
selectDChecks = [click.option("--selectDChecks", "selectDChecks", multiple=True, metavar="PROPERTY", help="Returns the filter in the filter property.")]
selectRelatedObject = [click.option("--selectRelatedObject", "selectRelatedObject", multiple=True, metavar="PROPERTY", help="Returns the action filter in the filter property.")]
select_alerts = [click.option("--select_alerts", "select_alerts", multiple=True, metavar="PROPERTY", help="Returns the action filter in the filter property.")]
searchByAny = [click.option("--searchByAny", "searchByAny", is_flag=True, help="Return results that match either filter or search instead of all of them")]
searchWildcardsEnabled = [click.option("--searchWildcardsEnabled", "searchWildcardsEnabled", is_flag=True, help="Enables use of '*' as a wildcard character")]
filter = [click.option("--filter", "filter", nargs=2, multiple=True, metavar="KEY VALUE", help="Return only results that exactly match the filter.")]
tags = [click.option("--tags", "tags", nargs=2, multiple=True, metavar="TAG VALUE", help="Return objects with given tags.")]
selectAcknowledgeOperations = [click.option("--selectAcknowledgeOperations", "selectAcknowledgeOperations", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectAcknowledges = [click.option("--selectAcknowledges", "selectAcknowledges", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectAlarms = [click.option("--selectAlarms", "selectAlarms", nargs=2, multiple=True, metavar="KEY VALUE", help="Returns the filter in the filter property.")]
selectApplicationPrototypes = [click.option("--selectApplicationPrototypes", "selectApplicationPrototypes", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectApplications = [click.option("--selectApplications", "selectApplications", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectDependencies = [click.option("--selectDependencies", "selectDependencies", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectDiscoveries = [click.option("--selectDiscoveries", "selectDiscoveries", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectFunctions = [click.option("--selectFunctions", "selectFunctions", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectGraphDiscovery = [click.option("--selectGraphDiscovery", "selectGraphDiscovery", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectGraphItems = [click.option("--selectGraphItems", "selectGraphItems", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectGraphs = [click.option("--selectGraphs", "selectGraphs", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectGroupDiscovery = [click.option("--selectGroupDiscovery", "selectGroupDiscovery", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectGroupLinks = [click.option("--selectGroupLinks", "selectGroupLinks", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectGroupPrototypes = [click.option("--selectGroupPrototypes", "selectGroupPrototypes", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectGroups = [click.option("--selectGroups", "selectGroups", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectHostDiscovery = [click.option("--selectHostDiscovery", "selectHostDiscovery", nargs=2, multiple=True, help="Returns the filter in the filter property.")]
selectHostPrototypes = [click.option("--selectHostPrototypes", "selectHostPrototypes", nargs=2, multiple=True, help="todo help")]
selectHttpTests = [click.option("--selectHttpTests", "selectHttpTests", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectIconMap = [click.option("--selectIconMap", "selectIconMap", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectInterface = [click.option("--selectInterface", "selectInterface", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectInterfaces = [click.option("--selectInterfaces", "selectInterfaces", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectInventory = [click.option("--selectInventory", "selectInventory", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectItemDiscovery = [click.option("--selectItemDiscovery", "selectItemDiscovery", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectLLDMacroPaths = [click.option("--selectLLDMacroPaths", "selectLLDMacroPaths", nargs=2, multiple=True, help="todo help")]
selectLastEvent = [click.option("--selectLastEvent", "selectLastEvent", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectLines = [click.option("--selectLines", "selectLines", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectLinks = [click.option("--selectLinks", "selectLinks", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectMacros = [click.option("--selectMacros", "selectMacros", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectMappings = [click.option("--selectMappings", "selectMappings", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectMedias = [click.option("--selectMedias", "selectMedias", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectParent = [click.option("--selectParent", "selectParent", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectParentDependencies = [click.option("--selectParentDependencies", "selectParentDependencies", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectParentHost = [click.option("--selectParentHost", "selectParentHost", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectParentTemplates = [click.option("--selectParentTemplates", "selectParentTemplates", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectPreprocessing = [click.option("--selectPreprocessing", "selectPreprocessing", nargs=2, multiple=True, help="Return a preprocessing property with LLD rule preprocessing options.")]
selectRights = [click.option("--selectRights", "selectRights", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectScreenItems = [click.option("--selectScreenItems", "selectScreenItems", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectScreens = [click.option("--selectScreens", "selectScreens", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectSelements = [click.option("--selectSelements", "selectSelements", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectShapes = [click.option("--selectShapes", "selectShapes", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectSteps = [click.option("--selectSteps", "selectSteps", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectSuppressionData = [click.option("--selectSuppressionData", "selectSuppressionData", nargs=2, multiple=True, help="Return a suppression_data property with the list of maintenances")]
selectTagFilters = [click.option("--selectTagFilters", "selectTagFilters", nargs=2, multiple=True, help="Return user group tag based permissions in the tag_filters ")]
selectTags = [click.option("--selectTags", "selectTags", nargs=2, multiple=True, help="Return tags in the tag property.")]
selectTemplates = [click.option("--selectTemplates", "selectTemplates", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectTimeperiods = [click.option("--selectTimeperiods", "selectTimeperiods", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectTimes = [click.option("--selectTimes", "selectTimes", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectTrigger = [click.option("--selectTrigger", "selectTrigger", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectTriggerDiscovery = [click.option("--selectTriggerDiscovery", "selectTriggerDiscovery", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectTriggers = [click.option("--selectTriggers", "selectTriggers", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectUrls = [click.option("--selectUrls", "selectUrls", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
selectUsrgrps = [click.option("--selectUsrgrps", "selectUsrgrps", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
select_acknowledges = [click.option("--select_acknowledges", "select_acknowledges", nargs=2, multiple=True, help="Returns the action filter in the filter property.")]
select_image = [click.option("--select_image", "select_image", is_flag=True, help="Return the Base64 encoded image in the image property.")]
actionids = [click.option("--actionid", "actionids", type=int, multiple=True, metavar="ID", help="Return objects with the given action id.")]
alertids = [click.option("--alertid", "alertids", type=int, multiple=True, metavar="ID", help="Return objects with the given alert id.")]
applicationids = [click.option("--applicationid", "applicationids", type=int, multiple=True, metavar="ID", help="Return objects with the given application id.")]
childids = [click.option("--childid", "childids", type=int, multiple=True, metavar="ID", help="Return objects with the given child id.")]
correlationids = [click.option("--correlationid", "correlationids", type=int, multiple=True, metavar="ID", help="Return objects with the given correlation id.")]
dashboardids = [click.option("--dashboardid", "dashboardids", type=int, multiple=True, metavar="ID", help="Return objects with the given dashboard id.")]
dcheckids = [click.option("--dcheckid", "dcheckids", type=int, multiple=True, metavar="ID", help="Return objects with the given dcheck id")]
dhostids = [click.option("--dhostid", "dhostids", type=int, multiple=True, metavar="ID", help="Return objects with the given dhost id")]
discoveryids = [click.option("--discoveryid", "discoveryids", type=int, multiple=True, metavar="ID", help="Return objects with the given discovery id.")]
druleids = [click.option("--druleid", "druleids", type=int, multiple=True, metavar="ID", help="Return only discovered hosts that have been created by the given discovery rules.")]
dserviceids = [click.option("--dserviceid", "dserviceids", type=int, multiple=True, metavar="ID", help="Return only discovered hosts that are running the given services.")]
eventids = [click.option("--eventid", "eventids", type=int, multiple=True, metavar="ID", help="Return objects that are configured to send messages to the given user groups.")]
gitemids = [click.option("--gitemid", "gitemids", type=int, multiple=True, metavar="ID", help="Return results with the given graphitem id.")]
globalmacroids = [click.option("--globalmacroid", "globalmacroids", type=int, multiple=True, metavar="ID", help="Return responses with the given globmacro id.")]
graphids = [click.option("--graphid", "graphids", type=int, multiple=True, metavar="ID", help="Return objects that use the given graph id.")]
groupids = [click.option("--groupid", "groupids", type=int, multiple=True, metavar="ID", help="Return responses that use the given groups.")]
hostids = [click.option("--hostid", "hostids", type=int, multiple=True, metavar="ID", help="Return responses that use the host id.")]
hostmacroids = [click.option("--hostmacroid", "hostmacroids", type=int, multiple=True, metavar="ID", help="Return responses with the given hostmacro id.")]
httptestids = [click.option("--httptestid", "httptestids", type=int, multiple=True, metavar="ID", help="Return responses with the given httptest id.")]
iconmapids = [click.option("--iconmapid", "iconmapids", type=int, multiple=True, metavar="ID", help="Return responses with the given iconmap id.")]
imageids = [click.option("--imageid", "imageids", type=int, multiple=True, metavar="ID", help="Return objects that use the given image id.")]
interfaceids = [click.option("--interfaceid", "interfaceids", type=int, multiple=True, metavar="ID", help="Return results with the given interface id")]
itemids = [click.option("--itemid", "itemids", type=int, multiple=True, metavar="ID", help="Return only actions that are configured to send messages to the given user groups.")]
maintenanceids = [click.option("--maintenanceid", "maintenanceids", type=int, multiple=True, metavar="ID", help="Return responses with the given maintenance id.")]
mediaids = [click.option("--mediaid", "mediaids", type=int, multiple=True, metavar="ID", help="Return responses with the given media id.")]
mediatypeids = [click.option("--mediatypeid", "mediatypeids", type=int, multiple=True, metavar="ID", help="Return objects that use the mediatype id.")]
nodeids = [click.option("--nodeid", "nodeids", type=int, multiple=True, metavar="ID", help="Return responses with the given node id.")]
objectids = [click.option("--objectid", "objectids", type=int, multiple=True, metavar="ID", help="Return only actions that are configured to send messages to the given user groups.")]
parentTemplateids = [click.option("--parentTemplateid", "parentTemplateids", type=int, multiple=True, metavar="ID", help="Return responses with the given parentTemplate id.")]
parentids = [click.option("--parentid", "parentids", type=int, multiple=True, metavar="ID", help="Return responses with the given parent id.")]
proxyids = [click.option("--proxyid", "proxyids", type=int, multiple=True, metavar="ID", help="Return only hosts that are monitored by the given proxies.")]
screenids = [click.option("--screenid", "screenids", type=int, multiple=True, metavar="ID", help="Return objects that use the given screen id.")]
screenitemids = [click.option("--screenitemid", "screenitemids", type=int, multiple=True, metavar="ID", help="Return objects that use the given screenitem id.")]
scriptids = [click.option("--scriptid", "scriptids", type=int, multiple=True, metavar="ID", help="Return only actions that are configured to run the given scripts.")]
serviceids = [click.option("--serviceid", "serviceids", type=int, multiple=True, metavar="ID", help="Return responses with the given service id.")]
sysmapids = [click.option("--sysmapid", "sysmapids", type=int, multiple=True, metavar="ID", help="Return objects with the given sysmap id.")]
templateids = [click.option("--templateid", "templateids", type=int, multiple=True, metavar="ID", help="Return objects with the given template id.")]
triggerids = [click.option("--triggerid", "triggerids", type=int, multiple=True, metavar="ID", help="Return objects with the given triggers id.")]
userids = [click.option("--userid", "userids", type=int, multiple=True, metavar="ID", help="Return only actions that are configured to send messages to the given users.")]
usrgrpids = [click.option("--usrgrpid", "usrgrpids", type=int, multiple=True, metavar="ID", help="Return only actions that are configured to send messages to the given user groups.")]
valuemapids = [click.option("--valuemapid", "valuemapids", type=int, multiple=True, metavar="ID", help="Return responses with the given valuemap id.")]
evaltype = [click.option("--evaltype", "evaltype", type=int, multiple=True, default=0, help="Rules for tag searching")]
eventobject = [click.option("--eventobject", "eventobject", default=0, help="Return objects generated by events related to objects of the given type.")]
eventsource = [click.option("--eventsource", "eventsource", default=0, help="Return objects generated by events of the given type")]
application = [click.option("--application", "application", help="Return only items that belong to an application with the given name.")]
functions = [click.option("--functions", "functions", help="Return only triggers that use the given functions.")]
group = [click.option("--group", "group", help="Return only items that belong to a group with the given name.")]
history = [click.option("--history", "history", type=int, help="History object types to return.")]
host = [click.option("--host", "host", help="Return only items that belong to a host with the given name.")]
limitSelects = [click.option("--limitSelects", "limitSelects", type=int, default=1000, help="Return objects generated by events of the given type")]
min_severity = [click.option("--min_severity", "min_severity", help="Return only triggers with severity greater or equal than the given severity.")]
object = [click.option("--object", "object", type=int, help="Return objects with the given type")]
recent = [click.option("--recent", "recent", help="return PROBLEM and recently RESOLVED problems")]
search = [click.option("--search", "search", nargs=2, multiple=True, help="Return results that match wildcard search (case-insensitive).")]
searchInventory = [click.option("--searchInventory", "searchInventory", help="Return only hosts that have inventory data matching the given wildcard search.")]
severities = [click.option("--severities", "severities", type=int, multiple=True, help="Return only objects with given trigger severities.")]
skipDependent = [click.option("--skipDependent", "skipDependent", is_flag=True, help="Skip triggers in a problem state that are dependent on other triggers")]
sortfield = [click.option("--sortfield", "sortfield", help="Sort the result by the given properties.")]
sortorder = [click.option("--sortorder", "sortorder", type=click.Choice(['ASC', 'DESC']), help="Order of sorting")]
source = [click.option("--source", "source", type=int, help="Return objects with the given type")]
startSearch = [click.option("--startSearch", "startSearch", is_flag=True, help="Compare from the beginning of fields.")]
status = [click.option("--status", "status", type=int, multiple=True, help="Return users with given status.")]
suppressed = [click.option("--suppressed", "suppressed", is_flag=True, default=False, help="return only suppressed events")]
value = [click.option("--value", "value", type=int, multiple=True, help="Return objects with given value.")]
type = [click.option("--type", "type", type=int, default=0, help="Return only graph items with the given type.")]


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options


def add_sortfield(options, *args):
    def _add_options(func, *args):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options
