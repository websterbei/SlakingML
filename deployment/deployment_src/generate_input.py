import numpy as np
import json

input_arr = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.12941177189350128,0.3764705955982208,0.686274528503418,0.6117647290229797,0.250980406999588,0.054901961237192154,0.21176470816135406,0.5372549295425415,0.800000011920929,0.7607843279838562,0.4000000059604645,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.2862745225429535,0.729411780834198,0.6941176652908325,0.7176470756530762,0.686274528503418,0.7372549176216125,0.9098039269447327,1.0,0.8745098114013672,0.8588235378265381,0.7607843279838562,0.7019608020782471,0.729411780834198,0.8352941274642944,0.572549045085907,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.13725490868091583,0.6392157077789307,0.5490196347236633,0.5882353186607361,0.5960784554481506,0.5882353186607361,0.572549045085907,0.686274528503418,0.686274528503418,0.6784313917160034,0.6705882549285889,0.6117647290229797,0.5960784554481506,0.5803921818733215,0.5058823823928833,0.6117647290229797,0.5490196347236633,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.5882353186607361,0.5568627715110779,0.5490196347236633,0.5960784554481506,0.6274510025978088,0.6117647290229797,0.572549045085907,0.5568627715110779,0.49803921580314636,0.529411792755127,0.5215686559677124,0.5490196347236633,0.5490196347236633,0.5372549295425415,0.5215686559677124,0.4901960790157318,0.6627451181411743,0.29411765933036804,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.21176470816135406,0.6549019813537598,0.572549045085907,0.5058823823928833,0.5568627715110779,0.5372549295425415,0.5372549295425415,0.5137255191802979,0.5803921818733215,0.5803921818733215,0.5215686559677124,0.5137255191802979,0.5137255191802979,0.5137255191802979,0.4901960790157318,0.5490196347236633,0.5490196347236633,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.4313725531101227,0.7372549176216125,0.5215686559677124,0.572549045085907,0.5960784554481506,0.5215686559677124,0.4901960790157318,0.49803921580314636,0.46666666865348816,0.5058823823928833,0.5215686559677124,0.46666666865348816,0.5490196347236633,0.5137255191802979,0.5882353186607361,0.054901961237192154,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.8666666746139526,0.6196078658103943,0.5372549295425415,0.529411792755127,0.48235294222831726,0.4313725531101227,0.4313725531101227,0.4470588266849518,0.42352941632270813,0.43921568989753723,0.4588235318660736,0.49803921580314636,0.5568627715110779,0.3019607961177826,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.01568627543747425,0.0,0.09803921729326248,0.6196078658103943,0.5372549295425415,0.4901960790157318,0.46666666865348816,0.46666666865348816,0.4313725531101227,0.4588235318660736,0.4588235318660736,0.4313725531101227,0.46666666865348816,0.49803921580314636,0.5647059082984924,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.48235294222831726,0.6117647290229797,0.5058823823928833,0.43921568989753723,0.4313725531101227,0.4000000059604645,0.43921568989753723,0.3921568691730499,0.4745098054409027,0.4588235318660736,0.5058823823928833,0.4470588266849518,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.4901960790157318,0.6627451181411743,0.49803921580314636,0.46666666865348816,0.4156862795352936,0.42352941632270813,0.40784314274787903,0.3686274588108063,0.4745098054409027,0.4470588266849518,0.5058823823928833,0.35686275362968445,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.007843137718737125,0.0,0.3843137323856354,0.6705882549285889,0.5058823823928833,0.43921568989753723,0.40784314274787903,0.4470588266849518,0.4156862795352936,0.4000000059604645,0.43921568989753723,0.40784314274787903,0.5215686559677124,0.250980406999588,0.0,0.01568627543747425,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.007843137718737125,0.0,0.25882354378700256,0.6784313917160034,0.529411792755127,0.5058823823928833,0.3843137323856354,0.3921568691730499,0.46666666865348816,0.4000000059604645,0.42352941632270813,0.3843137323856354,0.529411792755127,0.23529411852359772,0.0,0.01568627543747425,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.007843137718737125,0.0,0.21960784494876862,0.6705882549285889,0.529411792755127,0.49803921580314636,0.3921568691730499,0.42352941632270813,0.4588235318660736,0.3333333432674408,0.4156862795352936,0.4313725531101227,0.529411792755127,0.25882354378700256,0.0,0.01568627543747425,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.20392157137393951,0.5882353186607361,0.5058823823928833,0.4313725531101227,0.3921568691730499,0.35686275362968445,0.4000000059604645,0.3686274588108063,0.32549020648002625,0.40784314274787903,0.48235294222831726,0.25882354378700256,0.0,0.01568627543747425,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.007843137718737125,0.0,0.25882354378700256,0.6549019813537598,0.5490196347236633,0.5803921818733215,0.5803921818733215,0.49803921580314636,0.5372549295425415,0.5960784554481506,0.572549045085907,0.572549045085907,0.5803921818733215,0.3764705955982208,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.1764705926179886,0.48235294222831726,0.3686274588108063,0.40784314274787903,0.3764705955982208,0.46666666865348816,0.4745098054409027,0.4156862795352936,0.3843137323856354,0.43921568989753723,0.34117648005485535,0.4470588266849518,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.4156862795352936,0.3490196168422699,0.22745098173618317,0.19607843458652496,0.14509804546833038,0.19607843458652496,0.25882354378700256,0.21960784494876862,0.19607843458652496,0.29411765933036804,0.29411765933036804,0.5372549295425415,0.08627451211214066,0.0,0.007843137718737125,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.007843137718737125,0.0,0.11372549086809158,0.5803921818733215,0.4470588266849518,0.4156862795352936,0.4901960790157318,0.3490196168422699,0.3921568691730499,0.5215686559677124,0.4588235318660736,0.5137255191802979,0.5137255191802979,0.5137255191802979,0.4901960790157318,0.43921568989753723,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.3921568691730499,0.4156862795352936,0.4470588266849518,0.35686275362968445,0.5372549295425415,0.24313725531101227,0.4000000059604645,0.5137255191802979,0.3490196168422699,0.529411792755127,0.43921568989753723,0.5137255191802979,0.42352941632270813,0.529411792755127,0.14509804546833038,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.572549045085907,0.3921568691730499,0.42352941632270813,0.3843137323856354,0.5647059082984924,0.24313725531101227,0.4156862795352936,0.5137255191802979,0.34117648005485535,0.5215686559677124,0.40784314274787903,0.6274510025978088,0.4588235318660736,0.4745098054409027,0.2666666805744171,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.12941177189350128,0.4745098054409027,0.42352941632270813,0.3764705955982208,0.3921568691730499,0.5490196347236633,0.27843138575553894,0.4156862795352936,0.49803921580314636,0.3333333432674408,0.5490196347236633,0.40784314274787903,0.5882353186607361,0.5490196347236633,0.4470588266849518,0.3490196168422699,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.24313725531101227,0.46666666865348816,0.43921568989753723,0.4000000059604645,0.4313725531101227,0.5372549295425415,0.29411765933036804,0.4156862795352936,0.5647059082984924,0.3176470696926117,0.5647059082984924,0.42352941632270813,0.4588235318660736,0.6039215922355652,0.4588235318660736,0.40784314274787903,0.07058823853731155,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.25882354378700256,0.4745098054409027,0.4000000059604645,0.43921568989753723,0.4588235318660736,0.5137255191802979,0.2862745225429535,0.40784314274787903,0.6117647290229797,0.3019607961177826,0.5372549295425415,0.529411792755127,0.32549020648002625,0.7019608020782471,0.5058823823928833,0.4745098054409027,0.13725490868091583,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.3333333432674408,0.49803921580314636,0.3176470696926117,0.4901960790157318,0.5215686559677124,0.46666666865348816,0.30980393290519714,0.3921568691730499,0.6627451181411743,0.32549020648002625,0.5058823823928833,0.686274528503418,0.23529411852359772,0.6392157077789307,0.529411792755127,0.572549045085907,0.15294118225574493,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.4156862795352936,0.5058823823928833,0.24313725531101227,0.5490196347236633,0.5647059082984924,0.42352941632270813,0.3333333432674408,0.32549020648002625,0.6196078658103943,0.3333333432674408,0.5058823823928833,0.686274528503418,0.1882352977991104,0.572549045085907,0.5215686559677124,0.529411792755127,0.250980406999588,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.4588235318660736,0.46666666865348816,0.30980393290519714,0.5490196347236633,0.5960784554481506,0.4000000059604645,0.3490196168422699,0.4313725531101227,0.5372549295425415,0.3764705955982208,0.5882353186607361,0.7686274647712708,0.32549020648002625,0.5647059082984924,0.529411792755127,0.5215686559677124,0.3019607961177826,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.6039215922355652,0.4745098054409027,0.34117648005485535,0.5490196347236633,0.6039215922355652,0.43921568989753723,0.3686274588108063,0.20392157137393951,0.5568627715110779,0.3921568691730499,0.32549020648002625,0.5960784554481506,0.3333333432674408,0.6274510025978088,0.5215686559677124,0.3921568691730499,0.0470588244497776,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.01568627543747425,0.0,0.007843137718737125,0.0,0.13725490868091583,0.01568627543747425,0.12941177189350128,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
input_arr = np.reshape(input_arr,(1,-1))
with open("deployment_input", "w") as f:
    json.dump(input_arr.tolist(),f)