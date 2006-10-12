// -*- C++ -*-
//
// Package:    CaloMiscalibTools
// Class:      CaloMiscalibTools
// 
/**\class CaloMiscalibTools CaloMiscalibTools.cc CalibCalorimetry/CaloMiscalibTools/src/CaloMiscalibTools.cc

 Description: Definition of CaloMiscalibTools

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Lorenzo AGOSTINO
//         Created:  Mon Jul 17 18:07:01 CEST 2006
// $Id: AlCaElectronsProducer.h,v 1.2 2006/09/06 16:08:17 lorenzo Exp $
//
// Modified       : Luca Malgeri 
// Date:          : 11/09/2006 
// Reason         : split class definition (.h) from source code (.cc)
 

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/SourceFactory.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/ESProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Framework/interface/EventSetupRecordIntervalFinder.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "CondFormats/EcalObjects/interface/EcalIntercalibConstants.h"
#include "CondFormats/DataRecord/interface/EcalIntercalibConstantsRcd.h"
#include "CalibCalorimetry/CaloMiscalibTools/interface/CaloMiscalibMapEcal.h"

//
// class decleration
//

class CaloMiscalibTools : public edm::ESProducer, public edm::EventSetupRecordIntervalFinder  {
   public:
      CaloMiscalibTools(const edm::ParameterSet&);
      ~CaloMiscalibTools();

      typedef const  EcalIntercalibConstants * ReturnType;

      ReturnType produce(const EcalIntercalibConstantsRcd&);
   private:
      // ----------member data ---------------------------
    void setIntervalFor(const edm::eventsetup::EventSetupRecordKey &, const edm::IOVSyncValue&, edm::ValidityInterval & );
    
    CaloMiscalibMapEcal map_;
    std::string barrelfile_; 
    std::string endcapfile_; 
};
