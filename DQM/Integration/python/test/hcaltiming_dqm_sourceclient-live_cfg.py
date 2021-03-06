import FWCore.ParameterSet.Config as cms
process = cms.Process("HcalTimingTest")

process.load("DQM.Integration.test.inputsource_cfi")

print "Running with run type = ", process.runType.getRunType()

# Set this to True if running in Heavy Ion mode
HEAVYION=False
if runType == runTypes.hi_run:
      HEAVYION=True
      
process.DQMEventStreamHttpReader.consumerName = 'Hcal Timing DQM Consumer'

process.MessageLogger = cms.Service("MessageLogger",
     categories   = cms.untracked.vstring(''),
     destinations = cms.untracked.vstring('cout'),
     debugModules = cms.untracked.vstring('*'),
     cout = cms.untracked.PSet(
         threshold = cms.untracked.string('WARNING'),
         WARNING = cms.untracked.PSet(limit = cms.untracked.int32(0))
     )
)

process.load("EventFilter.HcalRawToDigi.HcalRawToDigi_cfi")

process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("L1Trigger.Configuration.L1DummyConfig_cff")
process.load("EventFilter.L1GlobalTriggerRawToDigi.l1GtUnpack_cfi")
process.l1GtUnpack.DaqGtInputTag = 'source'

process.load("DQM.HcalMonitorModule.HcalTimingModule_cfi")

#-----------------------------
# Hcal Conditions: from Global Conditions Tag 
#-----------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG"
process.GlobalTag.globaltag = 'GR_H_V37' # or any other appropriate
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')


### include to get DQM histogramming services
process.load("DQMServices.Core.DQM_cfg")
### set the verbose
process.DQMStore.verbose = 0
#### BEGIN DQM Online Environment #######################
### replace YourSubsystemName by the name of your source ###
### use it for dqmEnv, dqmSaver
process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_cfi")
### path where to save the output file
#process.dqmSaver.dirName = '.'
### the filename prefix
#process.dqmSaver.producer = 'DQM'
### possible conventions are "Online", "Offline" and "RelVal"
#process.dqmSaver.convention = 'Online'
process.dqmEnv.subSystemFolder = 'HcalTiming'

process.p = cms.Path(process.hcalDigis*process.l1GtUnpack*process.hcalTimingMonitor*process.dqmEnv*process.dqmSaver)

#--------------------------------------------------
# Heavy Ion Specific Fed Raw Data Collection Label
#--------------------------------------------------
if (HEAVYION):
    process.hcalDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.l1GtUnpack.DaqGtInputTag = cms.InputTag("rawDataRepacker")
    
