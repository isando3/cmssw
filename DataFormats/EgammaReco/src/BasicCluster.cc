#include "DataFormats/EgammaReco/interface/BasicCluster.h"

using namespace reco;

BasicCluster::BasicCluster( double energy, const Point& position, double chi2, const std::vector<DetId> usedHits, AlgoId algoID) :
   EcalCluster(energy,position), chi2_(chi2)
{
  usedHits_ = usedHits;
  algoId_ = algoID;
}


bool BasicCluster::operator<(const reco::BasicCluster &otherCluster) const
{
  if(otherCluster.energy() > energy()) 
    return false;
  else
    return true;
}

bool BasicCluster::operator==(const BasicCluster& rhs) const  
{
  
  float Ediff = fabs(rhs.energy() - energy());
  if (Ediff < 0.00000001) return true;
  else return false;

}
