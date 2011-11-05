from nose import tools
from dashvisor.backends import file

from test_dashvisor.cases import SupervisorTestCase



class TestFileBackend(SupervisorTestCase):
    def setUp(self):
        self.backend = file.Backend()

    def test_servers_are_loaded(self):
        tools.assert_equals(
            set(self.backend.servers.keys()),
            set(['localhost', '127.0.0.1'])
        )
        tools.assert_equals(
            self.backend.servers['localhost'].status,
            {}
        )

    def test_backed_refresh(self):
        self.backend.refresh()
        tools.assert_equals(
            self.backend.servers['localhost'].status.keys(),
            ['a:x', 'a:y', 'b:y', 'b:z', 'tail-everything:tail-everything']
        )
        tools.assert_equals(
            self.backend.servers['127.0.0.1'].status.keys(),
            ['j:j', 'k:k', 'l:l']
        )
