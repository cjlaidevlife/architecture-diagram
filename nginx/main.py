from diagrams import Diagram, Cluster
from diagrams.onprem.network import Nginx
from diagrams.onprem.compute import Server 
from diagrams.onprem.client import Client 
from diagrams.generic.network import Firewall


def main():
    """Simple Internet Client Access Proxy Server
    """

    graph_attr = {
        "fontsize": "45",
        "bgcolor": "#FFFFFF"
    }

    node_attr = {
        "fontsize": "15",
    }

    try: 
        print('[INFO] job is starting...')
        with Diagram("Public Service By Reverse Proxy Server", show=False, graph_attr=graph_attr, node_attr=node_attr, direction="LR"):
            outside       = Client("Internet") 
            firewall      = Firewall("Firewall")
            nat_server    = Server("NAT")

            with Cluster("Nginx Reverse Proxy"):
                reverse_proxy = Nginx("Proxy")
                service_01    = Server("Service 01")
                service_02    = Server("Service 02")
                service_03    = Server("Service 03")
                reverse_proxy - [service_01, service_02, service_03]

            outside >> firewall >> nat_server >> reverse_proxy

    except Exception as e:
        print("[ERROR] have some error!", e)
    else: 
        print("[INFO] job is success!")
    finally:
        print("[INFO] job is finished!!")


if __name__ == '__main__':
    main()