import asyncio
from aioquic.asyncio import serve
from aioquic.quic.configuration import QuicConfiguration
from aioquic.h3.connection import H3Connection

class HTTP3Server:
    def __init__(self, app, host, port, certfile, keyfile):
        self.app = app
        self.host = host
        self.port = port
        self.certfile = certfile
        self.keyfile = keyfile

    async def run(self):
        configuration = QuicConfiguration(
            alpn_protocols=["h3"],
            max_datagram_frame_size=65536,
        )
        configuration.load_cert_chain(self.certfile, self.keyfile)

        await serve(
            self.host,
            self.port,
            configuration=configuration,
            create_protocol=self.create_protocol,
        )

    def create_protocol(self):
        return H3Connection(self.app)

def run_server(app, host, port, certfile, keyfile):
    server = HTTP3Server(app, host, port, certfile, keyfile)
    asyncio.run(server.run())