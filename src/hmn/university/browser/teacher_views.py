from Products.CMFPlone.PloneBatch import Batch
from zope.publisher.browser import BrowserView


class TeacherList(BrowserView):
    """
    teacher list
    """

    def getQuery(self):
        sort_on = self.sort_on()
        path = "/".join(self.context.getPhysicalPath())
        query_dict = {
            "path": path,
            "portal_type": "Teacher",
            "depth": 1,
            "sort_on": sort_on,
            "sort_order": "reverse",
        }
        name = self.get_name()
        if name not in [None, ""]:
            query_dict["teacherName"] = name
        rank = self.get_rank()
        if rank not in [None, ""]:
            query_dict["facultyRank"] = rank

        return query_dict

    def getTeachers(self):
        b_start = self.batch_start()
        b_size = self.batch_size()
        query = self.getQuery()
        result = self.context.portal_catalog.searchResults(query)
        batch = Batch(result, b_size, int(b_start), orphan=0)
        return batch

    def get_name(self):
        value = self.request.get("name", None)
        return value

    def get_rank(self):
        value = self.request.get("rank", None)
        return value

    def sort_on(self):
        value = self.request.get("sort_on", "created")
        return str(value)

    def batch_start(self):
        value = self.request.get("b_start", 0)
        return int(value)

    def batch_size(self):
        b_size = 10
        if self.context.REQUEST.get("b_size", 10) not in (None, "", 10):
            b_size = self.context.REQUEST.get("b_size")
            if b_size == "all":
                b_size = 1000
            else:
                b_size = int(b_size)

        if (
            self.context.REQUEST.get("filterBy") == "lockable"
            or self.context.REQUEST.get("filterBy") == "confirmable"
        ):
            b_size = 1000
            self.context.REQUEST.set("b_size", "all")

        return b_size
