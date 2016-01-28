'use strict';
var fieldValues = {
  little_interest: null, 
  depression: null, 
  sleep_issues: null, 
  lethargy: null, 
  appetite_issues: null, 
  shame: null, 
  concentration_issues: null, 
  activity_change: null, 
  suicidal_thoughts: null
};

var QuestionFields = React.createClass({
  render: function() {
    return (
      <div className="col-sm-6 col-sm-offset-3">
        <p className="lead text-center">{this.props.description}</p>

        <button className="btn btn-success btn-lg btn-block" 
          name={this.props.questionName} 
          ref={this.props.questionName + "0"} value="0" 
          onClick={this.onZeroClickEvent}>
          Not at all
        </button>
        <button className="btn btn-default btn-lg btn-block" 
          name={this.props.questionName} 
          ref={this.props.questionName + "1"} value="1" 
          onClick={this.onOneClickEvent}>
          Several days
        </button>
        <button className="btn btn-warning btn-lg btn-block" 
          name={this.props.questionName} 
          ref={this.props.questionName + "2"} value="2" 
          onClick={this.onTwoClickEvent}>
          More than half the days
        </button>
        <button className="btn btn-danger btn-lg btn-block" 
          name={this.props.questionName} 
          ref={this.props.questionName + "3"} value="3" 
          onClick={this.onThreeClickEvent}>
          Nearly every day
        </button>
      </div>
    );
  },

  onZeroClickEvent: function() {
    var data = {};
    data[this.props.questionName] = this.refs[this.props.questionName + "0"].value;
    this.nextStep(data);
  }, 

  onOneClickEvent: function() {
    var data = {};
    data[this.props.questionName] = this.refs[this.props.questionName + "1"].value;
    this.nextStep(data);
  }, 

  onTwoClickEvent: function() {
    var data = {};
    data[this.props.questionName] = this.refs[this.props.questionName + "2"].value;
    this.nextStep(data);
  }, 

  onThreeClickEvent: function() {
    var data = {};
    data[this.props.questionName] = this.refs[this.props.questionName + "3"].value;
    this.nextStep(data);
  }, 

  nextStep: function(data) {
    this.props.saveValues(data);
    this.props.nextStep();
  }
});

class LittleInterestFields extends QuestionFields {}
class DepressionFields extends QuestionFields {}
class SleepIssuesFields extends QuestionFields {}
class LethargyFields extends QuestionFields {}
class AppetiteIssuesFields extends QuestionFields {}
class ShameFields extends QuestionFields {}
class ConcentrationIssuesFields extends QuestionFields {}
class ActivityChangeFields extends QuestionFields {}
class SuicidalThoughtsFields extends QuestionFields {}

var ContactButton = React.createClass({
  handleClick: function() {
    alert("Message has been sent.");
  }, 

  render: function() {
    return (
      <button className="btn btn-default btn-block" onClick={this.handleClick}>
        Contact
      </button>
    )
  }
});

var ResultsComponent = React.createClass({
  render: function() {
    var depressionSeverity = this.props.depressionSeverity();
    var severity = this.props.severity();

    if (depressionSeverity < 10) {
      return (
        <div className="col-sm-6 col-sm-offset-3">
          <div className="alert alert-info">
            <h3>Thank you very much</h3>
            <p><strong>Score:</strong> {depressionSeverity}</p>
            <p><strong>Severity:</strong> {severity}</p>
            <p>
              Based on your responses, we've assessed that you are experiencing 
              minimal symptoms of depression. However, it is our goal to 
              provide assistance to all patients. We have additional support 
              materials <a href="#">here</a> for further education, and we 
              recommend that you contact your doctor if you feel that your 
              symptoms are worsening.
            </p>
          </div>
        </div>
      );
    } else {
      return (
        <div className="col-sm-6 col-sm-offset-3">
          <div className="alert alert-warning">
            <h3>Thank you very much</h3>
            <p><strong>Score:</strong> {depressionSeverity}</p>
            <p><strong>Severity:</strong> {severity}</p>
            <p>
              Based on your responses, we've assessed that you are experiencing 
              significant symptoms of depression. When diagnosed as at a 
              moderate level, we advise the use of either antidepressants or 
              psychotherapy for treatment. 
            </p>
            <p>
              In cases where the symptoms are severe, the recommended treatment 
              is the use of both antidepressants and psychotherapy together.
            </p>
          </div>

          <div className="row">
            <h3 className="text-center">
              We found some therapists near you that can help with your 
              treatment
            </h3>

            <div className="col-sm-4">
              <div className="thumbnail">
                <img src="//placehold.it/300x200" alt="doctor" />
                <div className="caption">
                  <address>
                    <strong>John Doe</strong><br/>
                    123 Fake Street<br/>
                    New York, NY 10282<br/>
                    <abbr title="Phone">P:</abbr> 212-111-7777
                  </address>

                  <ContactButton />
                </div>
              </div>
            </div>

            <div className="col-sm-4">
              <div className="thumbnail">
                <img src="//placehold.it/300x200" alt="doctor" />
                <div className="caption">
                  <address>
                    <strong>Tim Bo</strong><br/>
                    45 River Road<br/>
                    Jersey City, NJ 07310<br/>
                    <abbr title="Phone">P:</abbr> 201-111-7777
                  </address>

                  <ContactButton />
                </div>
              </div>
            </div>

            <div className="col-sm-4">
              <div className="thumbnail">
                <img src="//placehold.it/300x200" alt="doctor" />
                <div className="caption">
                  <address>
                    <strong>Kim Jo</strong><br/>
                    111 Kings Road<br/>
                    New York, NY 10283<br/>
                    <abbr title="Phone">P:</abbr> 646-111-7777
                  </address>

                  <ContactButton />
                </div>
              </div>
            </div>

          </div>
        </div>
      );
    }
  }
});

var Questionnaire = React.createClass({
  getInitialState: function() {
    return {
      step: 1
    };
  }, 

  depressionSeverity: function() {
    var sum = 0;
    for (var prop in fieldValues) {
      sum += parseInt(fieldValues[prop]);
    }

    return sum;
  }, 

  severity: function() {
    var score = this.depressionSeverity();
    if (score < 5) {
      return "None";
    } else if (score < 10) {
      return "Mild";
    } else if (score < 15) {
      return "Moderate";
    } else if (score < 20) {
      return "Moderately Severe";
    } else if (score < 28) {
      return "Severe";
    } else {
      return "";
    }
  }, 

  saveValues: function(value) {
    return function() {
      fieldValues = Object.assign({}, fieldValues, value);
    }.bind(this)();
  }, 

  nextStep: function() {
    this.setState({
      step: this.state.step + 1
    });
  }, 

  previousStep: function() {
    this.setState({
      step: this.state.step - 1
    });
  }, 

  showStep: function() {
    switch (this.state.step) {
      case 1:
        return <LittleInterestFields 
          questionName="little_interest" 
          description="Little interest or pleasure in doing things?"
          fieldValues={fieldValues} 
          nextStep={this.nextStep} 
          saveValues={this.saveValues} />;
      case 2:
        return <DepressionFields 
          questionName="depression" 
          description="Feeling down, depressed, or hopeless?"  
          fieldValues={fieldValues} 
          nextStep={this.nextStep} 
          saveValues={this.saveValues} />;
      case 3:
        return <SleepIssuesFields 
          questionName="sleep_issues" 
          description="Trouble falling or staying asleep, or sleeping too much?"  
          fieldValues={fieldValues} 
          nextStep={this.nextStep} 
          saveValues={this.saveValues} />;
      case 4:
        return <LethargyFields 
          questionName="lethargy" 
          description="Feeling tired or having little energy?"  
          fieldValues={fieldValues} 
          nextStep={this.nextStep} 
          saveValues={this.saveValues} />;
      case 5:
        return <AppetiteIssuesFields 
          questionName="appetite_issues" 
          description="Poor appetite or overeating?"  
          fieldValues={fieldValues} 
          nextStep={this.nextStep} 
          saveValues={this.saveValues} />;
      case 6:
        return <ShameFields 
          questionName="shame" 
          description="Feeling bad about yourself -- or that you are a failure or have let yourself or your family down?"  
          fieldValues={fieldValues} 
          nextStep={this.nextStep} 
          saveValues={this.saveValues} />;
      case 7:
        return <ConcentrationIssuesFields 
          questionName="concentration_issues" 
          description="Trouble concentrating on things, such as reading the newspaper or watching television?" 
          fieldValues={fieldValues} 
          nextStep={this.nextStep} 
          saveValues={this.saveValues} />;
      case 8:
        return <ActivityChangeFields 
          questionName="activity_change" 
          description="Moving or speaking so slowly that other people could have noticed? Or the opposite -- being so fidgety or restless that you have been moving around a lot more than usual?" 
          fieldValues={fieldValues} 
          nextStep={this.nextStep} 
          saveValues={this.saveValues} />;
      case 9:
        return <SuicidalThoughtsFields 
          questionName="suicidal_thoughts" 
          description="Thoughts that you would be better off dead, or of hurting yourself in some way?" 
          fieldValues={fieldValues} 
          nextStep={this.nextStep} 
          saveValues={this.saveValues} />;
      case 10:
        return <ResultsComponent 
          depressionSeverity={this.depressionSeverity} 
          severity={this.severity} />;
    }
  }, 

  render: function() {
    return (
      <div className="row">
        {this.showStep()}
      </div>
    );
  }
});

ReactDOM.render(
  <Questionnaire />, 
  document.getElementById('phq9')
);
