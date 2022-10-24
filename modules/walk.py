class WalkRoute:

    def __init__(self, org, dst):
        self.org = tuple(org)
        self.dst = tuple(dst)
        self.map_link = self.generateMapLink()

    def generateMapLink(self):

        org_lat, org_lng = self.org
        dst_lat, dst_lng = self.dst

        return f"https://www.google.co.th/maps/dir/{org_lat},{org_lng}/{dst_lat},{dst_lng}/@{org_lat},{org_lng}"
    
    def createResponse(self):

        return {
            "WalkRoute" : {
                "org" : {
                    "location" : self.org
                },

                "dst" : {
                    "location" : self.dst
                },
                "map_link" : self.map_link
                }
            }

if __name__ == "__main__":

    org = (13.736758, 100.532412)
    dst = (13.73295646004718, 100.53057632482017)
    walk = WalkRoute(org, dst)
    print(walk.createResponse())