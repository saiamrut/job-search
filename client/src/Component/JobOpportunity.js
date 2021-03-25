import React from 'react';
import 'antd/dist/antd.css';
import { Table} from 'antd';


export default class JobOpportunity extends React.Component {
    constructor(props) {
        super(props);
        console.log(props)
        this.state = {
            boardId: props.match.params.boardId,
            jobSource: props.match.params.boardname,
            jobs: [],
            isPendingGetJobs: true
        }
        this.getData = this.getData.bind(this)
    }
    componentDidMount() {
        let url = `/jobs?jobBoardId=${this.state.boardId}`
        fetch(url).then((response) => response.json()).then(data => this.setState({ isPendingGetJobs: false, jobs: data }))
    }
    getData() {
        let data = []
        this.state.jobs.map(job => data.push(
            {
                "key": job.id,
                "id": job.id,
                "companyName": job.company_name,
                "jobTitle": job.job_title,
                "jobUrl": job.job_url
            }
        ))
        return data
    }
    getColumns() {
        return [
            {
                title: 'ID',
                dataIndex: 'id',
                key: 'id',
                width: 100,
                sorter: (a, b) => a.id - b.id
            },
            {
                title: 'Company Name',
                dataIndex: 'companyName',
                key: 'companyName',
                width: 100
            },
            {
                title: 'Job Title',
                dataIndex: 'jobTitle',
                key: 'jobTitle',
                width: 100
            },
            {
                title: 'Job URL',
                dataIndex: 'jobUrl',
                key: 'jobUrl',
                width: 100,
                render: (text, record) => <a href={record.jobUrl}>{text}</a>
            }
        ]
    }
    render() {

        return (
            <div>
                <h2>Job Source: {this.state.jobSource}</h2>
                <Table
                    dataSource={!this.state.isPendingGetJobs ? this.getData() : []}
                    columns={this.getColumns()}
                    loading={this.state.isPendingGetJobs}
                />
            </div>
        )
    }
}
