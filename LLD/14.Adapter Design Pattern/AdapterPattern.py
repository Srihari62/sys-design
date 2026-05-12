from abc import ABC, abstractmethod

# 1. Target interface expected by the client
class IReports(ABC):
    @abstractmethod
    def get_json_data(self, data: str) -> str:
        pass

# 2. Adaptee: provides XML data from a raw input
class XmlDataProvider:
    # Expect data in "name:id" format (e.g. "Alice:42")
    def get_xml_data(self, data: str) -> str:
        if ":" not in data:
            return "<error>Invalid format</error>"
        
        name, user_id = data.split(":", 1)
        # Build an XML representation
        return (f"<user>"
                f"<name>{name}</name>"
                f"<id>{user_id}</id>"
                f"</user>")

# 3. Adapter: implements IReports by converting XML → JSON
class XmlDataProviderAdapter(IReports):
    def __init__(self, provider: XmlDataProvider):
        self._xml_provider = provider

    def get_json_data(self, data: str) -> str:
        # 1. Get XML from the adaptee
        xml = self._xml_provider.get_xml_data(data)

        # 2. Naïvely parse out <name> and <id> values (matching C++ manual parsing logic)
        try:
            name = xml.split("<name>")[1].split("</name>")[0]
            user_id = xml.split("<id>")[1].split("</id>")[0]
        except (IndexError, ValueError):
            return "{\"error\":\"Parsing failed\"}"

        # 3. Build and return JSON
        return f'{{"name":"{name}", "id":{user_id}}}'

# 4. Client code works only with IReports
class Client:
    def get_report(self, report: IReports, raw_data: str) -> None:
        print(f"Processed JSON: {report.get_json_data(raw_data)}")

def main():
    # 1. Create the adaptee
    xml_prov = XmlDataProvider()

    # 2. Make our adapter
    adapter = XmlDataProviderAdapter(xml_prov)

    # 3. Give it some raw data
    raw_data = "Alice:42"

    # 4. Client prints the JSON
    client = Client()
    client.get_report(adapter, raw_data)
    # → Processed JSON: {"name":"Alice", "id":42}

if __name__ == "__main__":
    main()
