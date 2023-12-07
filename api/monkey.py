# for Python 3
from http.client import HTTPConnection

def _execute(self, url, method, data=None, add_headers=None):
        """Execute a request on the PrestaShop Webservice.

        :param url: full url to call
        :param method: GET, POST, PUT, DELETE, HEAD
        :param data: for PUT (edit) and POST (add) only,
                     the xml sent to PrestaShop
        :param add_headers: additional headers merged onto instance's headers.
        :return: tuple with (status code, header, content) of the response.
        """
        if add_headers is None:
            add_headers = {}

        request_headers = self.client.headers.copy()
        request_headers.update(add_headers)

        if self.verbose:
            currentlevel = HTTPConnection.debuglevel
            HTTPConnection.debuglevel = 1
        try:
            response = self.client.request(
                method,
                url,
                data=data,
                headers=request_headers,
                verify=False
            )
        finally:
            if self.verbose:
                HTTPConnection.debuglevel = currentlevel

        self._check_status_code(response.status_code, response.content)
        self._check_version(response.headers.get('psws-version'))

        return response