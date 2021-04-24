package com.javainuse.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;

@Entity
@Table(name = "Customer")
public class Customer {
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Id
	private String name;
	private long age;
	private String address;
	private String profession;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

}
