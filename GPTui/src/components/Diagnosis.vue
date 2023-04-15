<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <v-img contain height="300" src="@/assets/drGPT.jpg"/> 
      <h1 class="text-h2 font-weight-bold" style="margin-top: -46px; position: relative;">Dr. GPT</h1>

    
      <v-form v-model="valid">
        <v-container>
          <v-row>
            <v-col cols="12" md="4">
              <v-text-field v-model="firstname" :rules="nameRules" label="First name" required></v-text-field>
            </v-col>

            <v-col cols="12" md="4">
              <v-text-field v-model="lastname" :rules="nameRules" label="Last name" required>
              </v-text-field>
            </v-col>

            <v-col cols="12" md="4">
              <v-text-field v-model="age" :rules="ageRules" label="Age" required>
              </v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="4">
              <div style="text-align: left">Sex:</div>
                <v-radio-group v-model="sex" inline>
                  <v-radio label="Male" value="male"></v-radio> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <v-radio label="Female" value="female"></v-radio>
                </v-radio-group>
             </v-col>

            <v-col cols="12" md="4">
              <v-text-field v-model="height" :rules="heightRules" label="Height (in cm)" required>
              </v-text-field>
            </v-col>

            <v-col cols="12" md="4">
              <v-text-field v-model="weight" :rules="weightRules" label="Weight (in Kg)" required>
              </v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="4">
               <div style="text-align: left">Do you have any allergies?</div>
               <v-radio-group v-model="hasAllergies" inline>
                  <v-radio label="Yes" value="have allergies"></v-radio> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <v-radio label="No" value="no allergies"></v-radio>
                </v-radio-group>  
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="allergies" v-if="hasAllergies == 'have allergies'" label="Allergies">
              </v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="4">
               <div style="text-align: left">Were you diagnosed with any diseases?</div>
               <v-radio-group v-model="hasDisease" inline>
                  <v-radio label="Yes" value="have diseases"></v-radio> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <v-radio label="No" value="no diseases"></v-radio>
                </v-radio-group>  
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="disease" v-if="hasDisease == 'have diseases'" label="Diseases">
              </v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
      <v-form>
        <v-container>
          <v-row>
            <v-col cols="12" md="4">
               <div style="text-align: left">Do you have any Addictions?</div>
               <v-radio-group v-model="hasAddiction" inline>
                  <v-radio label="Yes" value="have addiction"></v-radio> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <v-radio label="No" value="no addiction"></v-radio>
                </v-radio-group>  
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="addiction" v-if="hasAddiction == 'have addiction'" label="Addictions">
              </v-text-field>            
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="frequencyAddiction" v-if="hasAddiction == 'have addiction'" label="Frequency">
              </v-text-field>  
            </v-col>
          </v-row>
        </v-container>
      </v-form>
      <v-form>
        <v-container>
          <v-row>
            <v-col cols="10" md="5">
               <div style="text-align: left">Which of the following Ailments do you have?</div>
               <v-radio-group v-model="Ailments" inline>
                  <v-radio label="Respiratory" value="has respiratory"></v-radio>
                  <v-radio label="Skin" value="has skin"></v-radio>
                  <v-radio label="Digestive" value="has digestive"></v-radio>
                  <v-radio label="Eye" value="has eye"></v-radio>
                  <v-radio label="Ear" value="has ear"></v-radio>
                </v-radio-group>
                <v-select chips v-model="ailmentRespiratory" v-if ="Ailments == 'has respiratory'" label="Select" :items="['Shortness of breath/Difficulty in breathing', 'Dry Cough', 'Cough which produces phlegm', 'Wheezing or whistling sound while breathing', 'Chest pain or discomfort', 'Fatigue or weakness', 'Fever or chills', 'Nasal congestion or runny nose','Soar throat or hoarness','Headache','Loss of smell and taste','Rapid breathing and Hyperventilation','Bluish lips or face','Shallow breath','Rapid Heartbeat','Difficulty speaking or swallowing','Sweating','Dizziness or light headedness','Confusion or disorientation','Swelling in legs or ankles','Chronic coughs persisting for weeks or months']" multiple></v-select> 
                <v-select chips v-model="ailmentSkin" v-if ="Ailments == 'has skin'" label="Select" :items="['Itching and Burning', 'Redness and Inflammation', 'Pain and Tenderness', 'Dryness and scaling', 'Blisters and pustules', 'Rashes and hives', 'Swelling', 'Crusting and scabbing', 'Changes inskin color or texture', 'Excessive sweating', 'Foul Odor', 'Hair Loss or Thinning','Ulcerations','Skin thickening','Fissures or Cracks in skin', 'Numbness or tingling','Flaking or peeling','Skin sensitivity','Photosensitivity']" multiple></v-select> 
                <v-select chips v-model="ailmentDigestive" v-if ="Ailments == 'has digestive'" label="Select" :items="['Abdominal Pain or discomfort', 'Bloating and gas', 'Nausea and vomitting', 'Diarrhea', 'Constipation', 'Acid reflux or heartburn','Difficulty Swallowing','Loss of appetite','Sudden Loss in weight','Fatigue or weakness','Yellowing of skin or eyes','Bloody or Tarry Stools','Recatal bleeding','Intolerance to certain foods','Excessive belching','Bad Breath or Halitosis','Metallic taste in mouth','Foul-smeling stools or Flatulence','Gastrointerstinal Bleeding','Difficulty breathing or Shortness of breath']" multiple></v-select> 
                <v-select chips v-model="ailmentEye" v-if ="Ailments == 'has eye'" label="Select" :items="['Blurred Vision', 'Double Vision', 'Loss of Vision','Vision loss in one eye', 'Redness and Irritation', 'Eye pain and discomfort', 'Sensitivity to light','Dry Eyes','watery Eyes','Eye discharge','Eye twitching','Swelling around the eye','Foreign body sensation in the eye','Flashes of light','Floaters','Distorted Vision','Halos around Light','Colour vision changes','Difficulty seeing at night']" multiple></v-select> 
                <v-select chips v-model="ailmentEar" v-if ="Ailments == 'has ear'" label="Select" :items="['Ear Pain', 'Ear Swelling', 'Ringing in the ears', 'Hearing loss', 'Vertigo or Dizziness', 'Itching in the ear','Swelling in the ear','Fullness or pressure in the ear','Nausae or vomiting associated with vertigo','Balance problems','Fever','Reduced Hearing sensitivity','Drainage from the ear','Earwax buildup','Sensitivity to sound','Facial weakness or Paralysis','Tenderness around the ear','Discomfort when moving the jaw','Reduced ability to differentiate sounds in noise','Jaw Pain']" multiple></v-select> 
            </v-col>
          </v-row>
        </v-container>
      </v-form>
      <div class="text-center">
        <v-dialog v-model="dialog" width="auto">
          <template v-slot:activator="{ props }">
            <v-btn color="primary" v-bind="props" @click = "getDiagnosis()">
              Submit
            </v-btn>
          </template>  
            <v-card>
              <v-card-text>
                <div v-if="patientReport == ''" class="text-center">
                  <v-progress-circular indeterminate color="primary"></v-progress-circular>
                  <div>(Avg. Waiting time is 2 minutes)</div>
                </div>
                <div v-if="patientReport != ''" v-html="patientReport"></div>
              </v-card-text>
                <v-card-actions v-if="patientReport != ''">
                  <v-btn color="primary" block @click=" dialog = false">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
      </div>
    </v-responsive>
  </v-container>
</template>

<script lang="ts">
export default {
    data: () => ({
      valid: false,
      firstname: '',
      lastname: '',
      nameRules: [
        (value: any) => {
          if (value) return true

          return 'Name is requred.'
        },
      ],
      age: '',
      ageRules: [
        (value: any) => {
          if (value) return true

          return 'Age is requred.'
        },
        (value: string) => {
          if (/^[1-9]\d*$/.test(value)) return true
          return 'Age must be valid.'
        },
      ],
      height: '',
      heightRules: [
        (value: any) => {
          if (value) return true

          return 'Height is requred.'
        },
        (value: string) => {
          if (/^[1-9]\d*$/.test(value)) return true
          return 'Height must be valid.'
        },
      ],
      weight: '',
      weightRules: [
        (value: any) => {
          if (value) return true

          return 'Weight is requred.'
        },
        (value: string) => {
          if (/^[1-9]\d*$/.test(value)) return true
          return 'Weight must be valid.'
        },
      ],
      sex: '',
      hasAllergies: '',
      allergies: '',
      disease: '',
      hasDisease:'',
      addiction: '',
      hasAddiction: '',  
      frequencyAddiction: '',
      Ailments: '',
      ailmentRespiratory:'',
      ailmentSkin:'',
      ailmentDigestive:'',
      ailmentEar:'',
      ailmentEye:'',
      symptoms:'',
      dialog: false,
      patientReport: '',
    }),
    methods: {
      getDiagnosis () {
        this.patientReport='';
        this.symptoms= `Respiratory symptoms are ${this.ailmentRespiratory != '' ? this.ailmentRespiratory : "None"}, Skin symptoms are ${this.ailmentSkin != '' ? this.ailmentSkin : "None"}, Digestive symptoms are ${this.ailmentDigestive != '' ? this.ailmentDigestive : "None"}, Ear symptoms are ${this.ailmentEar != '' ? this.ailmentEar : "None"}, Eye symptoms are ${this.ailmentEye != '' ? this.ailmentEye : "None"}`
        let patientDiagnosis = `I am ${this.firstname} ${this.lastname} an ${this.age} year old ${this.sex} of height ${this.height}cm and of weight ${this.weight}kg, I am allergic to ${this.allergies}, addicted to ${this.addiction} with a frequency of ${this.frequencyAddiction} and have been previously diagnosed with ${this.disease}. I currently am suffering from the following ${this.symptoms}` ;
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ result: patientDiagnosis }),
        };
          fetch("http://localhost:5000/get_advice", requestOptions)
          .then((response) => response.text())
          .then((data) => (this.patientReport = data));
        }
      
    },
    // beforeMount: function () {
    //   this.firstname = 'Gun';
    //   this.lastname = 'Boom';
    //   this.age = '19';
    //   this.height = '170';
    //   this.weight = '90';
    //   this.sex = 'male';
    //   this.hasAllergies = 'have allergies';
    //   this.allergies = 'Peanut and Pollen';
    //   this.disease = 'Diabetes A';
    //   this.hasDisease = 'have diseases';
    //   this.addiction = 'Smoking';
    //   this.hasAddiction = 'have addiction';
    //   this.frequencyAddiction = 'One per day';
    //   this.Ailments = 'has respiratory';
    //   this.ailmentRespiratory = 'Dry Cough';
    //   this.ailmentSkin = '';
    //   this.ailmentDigestive = '';
    //   this.ailmentEar = '';
    //   this.ailmentEye = '';
    // }
  }

</script>
