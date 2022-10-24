import geopy.distance

class BeamRoute:

    def __init__(self, org, dst):
        self.org = tuple(org)
        self.dst = tuple(dst)
        self.station =  {
                (13.736575, 100.531838) : "Jakkrapong yard",
                (13.736094, 100.531109) : "Faculty of Science",
                (13.734657, 100.531021) : "Faculty of Commerce and Accountancy",
                (13.733358, 100.530859) : "Chamchuri Square",
                (13.739253, 100.533251) : "Faculty of Arts",
                (13.739534, 100.531337) : "Faculty of Architect",
                (13.737290, 100.534074) : "Faculty of Engineering",
                (13.734325, 100.533342) : "Faculty of Political Science"
            }
        self.station_list = list(self.station.keys())
        self.org_station = self.getNearestStation(self.org)
        self.dst_station = self.getNearestStation(self.dst)
        self.map_link = self.generateMapLink()

    def getNearestStation(self, node):
        nlist = list()
        for station in self.station_list:
            nlist.append(geopy.distance.geodesic(node, station).km)

        distance = min(nlist)
        index = nlist.index(distance)
        station_location = self.station_list[index]
        station_name = self.station[station_location]

        return {
            "distance" : distance,
            "station_name" : station_name,
            "station_location" : station_location
        }

    def generateMapLink(self):

        org_lat, org_lng = self.org_station["station_location"]
        dst_lat, dst_lng = self.dst_station["station_location"]

        return f"https://www.google.co.th/maps/dir/{org_lat},{org_lng}/{dst_lat},{dst_lng}/@{org_lat},{org_lng}"
    
    def createResponse(self):

        return {
            "BeamRoute" : {
                "org" : {
                    "station_name" : self.org_station["station_name"],
                    "station_location" : self.org_station["station_location"]
                },

                "dst" : {
                    "station_name" : self.dst_station["station_name"],
                    "station_location" : self.dst_station["station_location"]
                },
                "map_link" : self.map_link
                }
            }

if __name__ == "__main__":

    org = (13.736758, 100.532412)
    dst = (13.73295646004718, 100.53057632482017)
    beam = BeamRoute(org, dst)
    print(beam.createResponse())