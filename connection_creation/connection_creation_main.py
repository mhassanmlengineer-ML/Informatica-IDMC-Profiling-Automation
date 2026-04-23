from connection_creation.connection_creator import ConnectionCreator
from user_login.login import Login
from configuration_manager.configuration_manager import ConfigurationManager


def main():
    systems_dict = {
        # "172.16.0.222": {
        #     "port": 2433,
        #     "systems": ["GIS"],
        #     "databases": [
        #                     "PRDGIS",
        #                     "PRDGIS_3D",
        #                     "PRDGIS_copy",
        #                     "PRDGIS_Design",
        #                     "PRDGIS_Survey",
        #                     "PRDGIS_testdba",
        #                     "WEBGIS"]},
                                 
        # "172.16.0.223": 
        # {
        #     "port": 2433,
        #     "systems": ["GIS"],
        #     "databases": [
        #                   "GISAudit",
        #                   "PRDGIS",
        #                   "PRDGIS_3D",
        #                   "PRDGIS_Copy",
        #                   "PRDGIS_Design",
        #                   "PRDGIS_New",
        #                   "PRDGIS_Survey",
        #                   "PRDGIS2D",
        #                   "PrdGISNew",
        #                   "PrdGISNewQC",
        #                   "StgPrdGISNew",
        #                   "WEBGIS"]
        # },

        # "172.16.0.67":
        # {
        #     "port": 5533,
        #     "systems": ["External Web Site"],
        #     "databases": [
        #         "MODON_Sitecore_Custom_PROD",
        #         "XP1_MarketingAutomation",
        #         "XP1_Messaging",
        #         "XP1_Processing.Pools",
        #         "XP1_ReferenceData",
        #         "XP1_Xdb.Collection.ShardMapManager",
        #         "XP1_Xdb.Collection.Shard0",
        #         "XP1_Xdb.Collection.Shard1",
        #         "XP1_ProcessingEngineTasks",
        #         "XP1_ProcessingEngineStorage",
        #         "XP1_Reporting",
        #         "XP1_Core",
        #         "XP1_Master",
        #         "XP1_Web",
        #         "XP1_ExperienceForms",
        #         "XP1_EXM.Master",
        #         "XP1_Processing.Tasks"
        #     ]
        # },

        # "172.16.10.183":
        # {
        #     "port": 1433,
        #     "systems": ["BI"],
        #     "databases": ["SSISDB"]
        # },

        # "172.16.10.150":
        # {
        #     "port": 1433,
        #     "systems": ["BI"],
        #     "databases": ["REPORTSERVER"]
        # },


        "172.16.0.169":
        {
            "port": 1433,
            "systems": ["Apollo System"],
            "databases": ["Apacs34", "Apacs34_New"]
        },

        # "172.16.0.169":
        # {
        #     "port": 1433,
        #     "systems": ["Suprema System"],
        #     "databases": ["Bio_AC", "Bio_TA", "Bio_VE", "ModonBiostarEvents"]
        # },
    
    # "172.16.0.169":
    #     {
    #         "port": 1433,
    #         "systems": ["ChatBot"],
    #         "databases": ["chatbot", "chatbot-ch"]
    #     },

    #     "172.16.0.251":
    #      {
    #         "port": 2333,
    #         "systems": ["Source Control"],
    #         "databases": ["AzureDevOps_Configuration", "AzureDevOps_ModonCollection"]
    #     }
    }

    config_mngr = ConfigurationManager()

    username = config_mngr.username
    password = config_mngr.password

    user_login = Login(username=username, password=password)
    session_id = user_login.user_login()

    connection_creator = ConnectionCreator(session_id=session_id)

    body = {
        "@type": "connection",
        "orgId": "01006L",
        "name": "",
        "description": "",
        "agentId": "01006L0800000000001H",
        "runtimeEnvironmentId": "01006L2500000000004A",
        "instanceName": "",
        "instanceDisplayName": "SqlServer",
        "host": "",
        "database": "",
        "codepage": "UTF-8",
        "authenticationType": "SqlServer",
        "adjustedJdbcHostName": "",
        "schema": "dbo",
        "shortDescription": "",
        "type": "SqlServer2019",
        "baseType": "SqlServer",
        "subType": "SqlServer2019",
        "port": "",
        "password": "Indorm@.tic@@_Sa@..69826",
        "username": "Informatica_sa",
        "timeout": 60,
        "connParams": {
            "agentId": "01006L0800000000001H",
            "agentGroupId": "01006L2500000000004A",
            "AUTHENTICATION_TYPE": "SqlServer",
            "orgId": "01006L"
        },
        "internal": False,
        "retryNetworkError": False,
        "supportsCCIMultiGroup": False,
        "metadataBrowsable": True,
        "supportLabels": False,
        "vaultEnabled": False,
        "vaultEnabledParams": [],
        "isRtAttrsRefreshRequired": False
    }

    for host, details in systems_dict.items():
        port = details["port"]
        systems = details["systems"]
        databases = details["databases"]

        for system in systems:
            for db in databases:
                
                body["name"] = f"{system}_{db}"
                body["host"] = host
                body["database"] = db
                body["port"] = port

                connection_creator.create_connection(body=body)



if __name__ == "__main__":
    main()


